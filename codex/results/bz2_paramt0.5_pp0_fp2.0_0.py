from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.BZ2File
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(b'hello world')

with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read())

# bz2.open()
with bz2.open('file.bz2', 'wt') as f:
    f.write('hello world')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# gzip
import gzip
with gzip.open('file.gz', 'wt') as f:
    f.write('hello world')

with gzip.open('file.gz', 'rt') as f:
    print(f.read())

with gzip.open('file.gz', 'rb') as f:
    print(f.read())
