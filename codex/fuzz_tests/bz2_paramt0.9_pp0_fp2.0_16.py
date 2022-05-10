from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(FTP_SOURCE)

# create md5 checksum
import hashlib
ftp_md5 = hashlib.md5(FTP_SOURCE).hexdigest()
ftp_md5

# compare checksums
import os
os.path.getsize('/mnt/tcga_data/tcga_data.tar.bz2')

# initiate download from node C via SFTP
from paramiko import Transport, SFTPClient, AutoAddPolicy
trans = Transport(('node-c', 22))
trans.connect(username = 'test', password = 'test_password')
sftp = SFTPClient.from_transport(trans)
sftp.get(remote_path='/mnt/tcga_data/tcga_data.tar.bz2'
         ,local_path='/mnt/sftp_download/tcga_data.tar.bz2')
sftp.close()
trans.close()

# double check filesize
import os
os.path.getsize('/mnt/sftp_download/
