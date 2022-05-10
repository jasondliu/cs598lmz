import bz2
bz2_file = bz2.BZ2File("/Users/sarah/Desktop/python/data/data.json.bz2")
data = bz2_file.read()
bz2_file.close()
data

# gzip
import gzip
gzip_file = gzip.open("/Users/sarah/Desktop/python/data/data.json.gz")
data = gzip_file.read()
gzip_file.close()
data

# lzma
import lzma
lzma_file = lzma.open("/Users/sarah/Desktop/python/data/data.json.xz")
data = lzma_file.read()
lzma_file.close()
data

# tar
import tarfile
tar_file = tarfile.open("/Users/sarah/Desktop/python/data/data.tar.gz")
data = tar_file.extractfile("data.json")
data = data.read()
tar_file.close()
data

# zip
import zipfile
zip_
