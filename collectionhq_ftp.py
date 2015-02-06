import os
from datetime import date
import zipfile
from ftplib import FTP

zipped = False
host = os.environ.get('collectionhq_host')
user = os.environ.get('collectionhq_user')
password = os.environ.get('collectionhq_password')
local_directory = 'C:\\ProgramData\\Polaris\\SrServiceRoot\\hermione\\37\\scheduledjobs'
filename_trunc = 'bib_Collection HQ data export_{}'.format(date.today().strftime('%m%d%Y'))
filename = ''
for f in os.listdir(local_directory):
    if f.startswith(filename_trunc): filename = f
    
def zip_file(filename, directory):
    full_filename = '{}\\{}'.format(directory, filename)
    zip_filename = filename.split('.')[0]+'.zip'
    zf = zipfile.ZipFile(zip_filename, mode='w')
    try:
        zf.write(full_filename, filename)
    finally:
        zf.close()
    return zip_filename

def ftp_put(host, user, password, filename, directory):
    full_filename = '{}\\{}'.format(directory, filename)
    ftp = FTP(host, user, password)
    with open(full_filename, 'rb') as f:
        ftp.storbinary('STOR {}'.format(filename), f)

if filename:
    if zipped:
        filename = zip_file(filename, local_directory)
        local_directory = '.'
    ftp_put(host, user, password, filename, local_directory)
    if zipped:
        os.remove(filename)
