import bz2
bz2_file = bz2.BZ2File('/tmp/test.bz2')
type(bz2_file)

bz2_file.read()

with bz2.open('/tmp/test.bz2', 'wt') as f:
    f.write('hello world')

with bz2.open('/tmp/test.bz2', 'rt') as f:
    data = f.read()

print(data)


import zipfile
zip_file = zipfile.ZipFile('/tmp/test.zip')
type(zip_file)

zip_file.namelist()

info = zip_file.getinfo('test.txt')
info.file_size
info.compress_size

from zipfile import ZipFile
from zipfile import ZipInfo

z = ZipFile('/tmp/test.zip', 'w')
z.write('/tmp/test.txt', arcname='test.txt')
z.writestr(ZipInfo('test2.txt'), 'content2')
z.close()


