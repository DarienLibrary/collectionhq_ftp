import os
from datetime import date, datetime
from ftplib import FTP

host = os.environ.get('collectionhq_host')
user = os.environ.get('collectionhq_user')
password = os.environ.get('collectionhq_password')
local_directory = r'C:\ProgramData\Polaris\SrServiceRoot\Ginny\37\scheduledjobs'
filename_truncs = ['bib_Collection HQ data export_{}'.format(date.today().strftime('%m%d%Y')),
		   'bib_Collection HQ Monthly_{}'.format(date.today().strftime('%m%d%Y'))]
logfile = 'log_collectionhq.txt'
filename = ''
for f in os.listdir(local_directory):
	for filename_trunc in filename_truncs:
	    if f.startswith(filename_trunc): filename = f

def ftp_put(host, user, password, filename, directory):
    ftp = FTP(host, user, password)
    with open(full_filename, 'rb') as f:
        ftp.storbinary('STOR {}'.format(filename), f)
    with open(logfile, 'a') as f:
        f.write('{}: {} uploaded from {}\n'.format(datetime.now(), filename, directory))

if filename:
    full_filename = r'{}\{}'.format(local_directory, filename)
    ftp_put(host, user, password, filename, local_directory)
    os.remove(full_filename)
else:
    with open(logfile, 'a') as f:
        f.write('{}: File not found to upload\n'.format(datetime.now()))
