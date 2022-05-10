import bz2
bz2_file = bz2.BZ2File('test.bz2', 'w')
bz2_file.write(data)
bz2_file.close()
bz2_file = bz2.BZ2File('test.bz2', 'r')
bz2_file.read()

import gzip
gzip_file = gzip.GzipFile('test.gz', 'w')
gzip_file.write(data)
gzip_file.close()
gzip_file = gzip.GzipFile('test.gz', 'r')
gzip_file.read()

import zipfile
zip_file = zipfile.ZipFile('test.zip', 'w')
zip_file.write('test.txt')
zip_file.close()
zip_file = zipfile.ZipFile('test.zip', 'r')
zip_file.read('test.txt')

import tarfile
tar_file = tarfile.TarFile('test.tar', 'w')
tar_file.add('test.txt')
tar_file.
