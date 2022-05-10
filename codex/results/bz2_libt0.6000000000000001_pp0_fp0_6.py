import bz2
bz2_file = bz2.BZ2File('data/test.xml.bz2')
for line in bz2_file:
    print(line)

# gzip
import gzip
gzip_file = gzip.GzipFile('data/test.xml.gz')
for line in gzip_file:
    print(line)

# zip
import zipfile
zip_file = zipfile.ZipFile('data/test.xml.zip')
for line in zip_file.open('test.xml'):
    print(line)

# tar
import tarfile
tar_file = tarfile.open('data/test.xml.tar')
for line in tar_file.extractfile('test.xml'):
    print(line)
