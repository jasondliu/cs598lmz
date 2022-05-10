from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.open()
with bz2.open('file.bz2', 'wt') as f:
    f.write(text)
with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# lzma
import lzma
with lzma.open('file.xz', 'wt') as f:
    f.write(text)
with lzma.open('file.xz', 'rt') as f:
    print(f.read())

# gzip
import gzip
with gzip.open('file.gz', 'wt') as f:
    f.write(text)
with gzip.open('file.gz', 'rt') as f:
    print(f.read())
