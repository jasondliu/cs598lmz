import bz2
bz2file = bz2.BZ2File('../data/train.csv.bz2')
bz2file.readline()

for i in range(10):
    print(bz2file.readline())

del bz2file

#%%
import gzip
gzipfile = gzip.GzipFile('../data/train.csv.gz')
gzipfile.readline()
for i in range(10):
    print(gzipfile.readline())
del gzipfile

#%%
import zipfile
zfile = zipfile.ZipFile('../data/train.csv.zip')
zfile.namelist()

csvfile = zfile.open('train.csv')
csvfile.readline()

for i in range(10):
    print(csvfile.readline())
del csvfile

#%%
import lzma
xzfile = lzma.LZMAFile('../data/train.csv.xz')
xzfile.readline()
for i in range(10):
    print(xzfile
