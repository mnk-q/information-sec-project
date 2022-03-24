import os
from math import sqrt
import librosa
import numpy as np


BUFFER_SIZE = 8192
MAX_BUFFER_POOL = 10400


def process(filepath, output_dir):
    dataset, file_system = librosa.load(filepath, sr=16000, mono=True, dtype=np.float64)
    dataset = sqrt(dataset/(dataset.var()/0.005))
    dataset_abs = np.abs(dataset)
    avepool_dataset_abs = dataset_abs[:dataset_abs.shape[0]//MAX_BUFFER_POOL *
                                MAX_BUFFER_POOL].reshape([-1, MAX_BUFFER_POOL]).mean(axis=1)

    cutoff_points = np.int16(avepool_dataset_abs < 0.005)
    audio_begin = np.zeros_like(cutoff_points)
    audio_end = np.zeros_like(cutoff_points)
    for i in range(len(cutoff_points)-1):
        audio_begin[i] = cutoff_points[i] - cutoff_points[i+1] > 0
        audio_end[i+1] = cutoff_points[i] - cutoff_points[i+1] < 0

    audio_begin = np.nonzero(audio_begin)[0]
    audio_end = np.nonzero(audio_end)[0]

    if audio_begin[0] >= audio_end[0]:
        audio_end = audio_end[1:]
    if audio_begin[-1] >= audio_end[-1]:
        audio_begin = audio_begin[:-1]

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(len(audio_end)):
        begin = audio_begin[i]
        end = audio_end[i]
        tmp = dataset[begin*MAX_BUFFER_POOL:end*MAX_BUFFER_POOL]
        out_path = os.path.join(output_dir, filepath.split(
            '/')[-1].replace('.', '_{}.'.format(i)))
        librosa.output.write_wav(out_path, tmp, file_system)