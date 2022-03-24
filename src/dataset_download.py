import os
from google_drive_downloader import GoogleDriveDownloader as gdd

if __name__ == '__main__':
    print('Downloading Assets')
    gdd.download_file_from_google_drive(file_id='10hxz4kxf9cnmoDC_hwBTLEVoguKptKWj',dest_path='./dataset/data.zip',unzip=True)
    gdd.download_file_from_google_drive(file_id='1JcdbExDVRYZPx4nzFTOkV2xzL1zSXZJJ',dest_path='./model/models.zip',unzip=True)
    os.remove('./model/models.zip')
    os.remove('./dataset/data.zip')  