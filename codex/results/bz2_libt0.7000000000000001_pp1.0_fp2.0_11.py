import bz2
bz2.BZ2File()


import zipfile
zf = zipfile.ZipFile('zipfile_write.zip', mode='w')
try:
    zf.write('README.md')
finally:
    zf.close()

zf = zipfile.ZipFile('zipfile_write.zip', mode='r')
try:
    zf.extractall()
finally:
    zf.close()


from zipfile_infolist import print_info
print_info('zipfile_write.zip')

from zipfile_namelist import print_info
print_info('zipfile_write.zip')

from zipfile_read import print_info
print_info('zipfile_write.zip')


from zipfile_write_compression import print_info
print_info('zipfile_write_compression.zip')


from zipfile_write_append import print_info
print_info('zipfile_write_append.zip')

from zipfile_write_append_str import print_info
print_info('zipfile_write
