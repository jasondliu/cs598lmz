import bz2
bz2_file = bz2.BZ2File('test.txt.bz2')
data = bz2_file.read()
bz2_file.close()
print(data)

# gzip
import gzip
gzip_file = gzip.GzipFile('test.txt.gz')
data = gzip_file.read()
gzip_file.close()
print(data)

# zip
import zipfile
zip_file = zipfile.ZipFile('test.zip')
data = zip_file.read('test.txt')
zip_file.close()
print(data)

# tar
import tarfile
tar_file = tarfile.open('test.tar.gz')
data = tar_file.extractfile('test.txt').read()
tar_file.close()
print(data)
