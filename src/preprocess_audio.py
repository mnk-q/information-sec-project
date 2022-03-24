import os
from split_files import process

if __name__ == '__main__':

    dataset_dir = './dataset/target_raw/'

    filepathes = [os.path.join(dataset_dir, f) for f in os.listdir(dataset_dir)]
    filepathes.sort()

    print('Splitting speech dataset ')
    process(filepathes[0], output_dir='./dataset/target/train_conversion')

    for filepath in filepathes[4:7]:
        process(filepath, output_dir='./dataset/target/train_verification')

    for filepath in filepathes[1:4]:
        process(filepath, output_dir='./dataset/target/test')
    
