import bz2
bz2_file = bz2.BZ2File("data/log.txt.bz2")
data = bz2_file.read()
bz2_file.close()
print(type(data))

import gzip
gz_file = gzip.open("data/log.txt.gz", mode="rt")
data = gz_file.read()
gz_file.close()
print(type(data))

import lzma
lzma_file = lzma.open("data/log.txt.xz")
data = lzma_file.read()
lzma_file.close()
print(type(data))

import zipfile
zip_file = zipfile.ZipFile("data/sample.zip")
data = zip_file.read("log.txt")
zip_file.close()
print(type(data))

import tarfile
tar_file = tarfile.open("data/sample.tar.gz")
data = tar_file.extractfile("log.txt")
tar_file.close()
print(type(data
