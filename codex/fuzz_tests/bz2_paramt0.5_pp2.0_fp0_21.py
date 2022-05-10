from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)
import gzip
with gzip.open('./data/ch09/example.gz', 'rb') as f:
    print(f.read())

with gzip.open('./data/ch09/example.gz', 'rt', encoding='utf-8') as f:
    print(f.read())

with gzip.open('./data/ch09/example.gz', 'wt') as f:
    f.write(text)

with gzip.open('./data/ch09/example.gz', 'wt') as f:
    f.write(text * 10)

import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)

import shutil
shutil.copyfile('./data/ch09/example.gz', './data/ch09/example_copy.gz')

with gzip.open
