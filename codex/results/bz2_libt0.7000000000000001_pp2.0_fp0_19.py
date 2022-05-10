import bz2
bz2_file = bz2.BZ2File('data/quotes.bz2')
bz2_file.read()

with bz2.open('data/quotes.bz2') as bz2_file:
    text = bz2_file.read()
    print(text)

#gzip
import gzip
with gzip.open('data/quotes.gz') as gz_file:
    text = gz_file.read()
    print(text)

#lzma
import lzma
with lzma.open('data/quotes.xz') as xz_file:
    text = xz_file.read()
    print(text)

#zip
import zipfile
with zipfile.ZipFile('data/quotes.zip') as zip_file:
    text = zip_file.read('quotes.txt')
    print(text)

#tar
import tarfile
with tarfile.open('data/quotes.tar') as tar_file:
    text = tar_file.extract
