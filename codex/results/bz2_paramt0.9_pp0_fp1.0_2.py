from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\0\x0f\x1f\x86\x9c')

import bz2
idx = 0
bz_file = bz2.BZ2File('example.bz2')

idx = 0
bz_file = bz2.BZ2File('example.bz2')
for line in iter(bz_file.readline, b''):
    idx += 1
    if idx >= 4:
        print(line.decode())
        break

bz_file.close()

# gzip compression
import gzip

s = b'witch which has which witches wrist watch'

f = gzip.GzipFile(mode='wb', compresslevel=1, fileobj=None)

compressed = f.compress(s)
compressed += f.flush()

f.close()

with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# pickle

