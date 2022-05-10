import bz2
bz2.BZ2File(filename)

# gzip
import gzip
gzip.open(filename)

# lzma
import lzma
lzma.open(filename)

# zip
import zipfile
zipfile.ZipFile(filename)

# tar
import tarfile
tarfile.open(filename)

# read file
with open(filename) as f:
    lines = f.readlines()

# write file
with open(filename, 'w') as f:
    f.write('')

# read file by line
with open(filename) as f:
    for line in f:
        print(line)

# read file by chunk
with open(filename) as f:
    chunk_size = 1024
    chunk = f.read(chunk_size)
    while chunk:
        print(chunk)
        chunk = f.read(chunk_size)

# read file by line and chunk
with open(filename) as f:
    for line in f:
        chunk_size = 1024
        chunk = f.read
