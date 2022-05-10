from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.open()
with bz2.open('file.bz2', 'wt') as f:
    f.write(text)

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# zlib.compress()
s = b'witch which has which witches wrist watch'
len(s)

import zlib
t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# zlib.compress()
import zlib
data = b'witch which has which witches wrist watch'
len(data)

compressed = zlib.compress(data)
len(compressed)

compressed

decompressed = zlib.decompress(compressed)
decompressed

# zlib.compress()
import zlib
data = b'witch which has which witches wrist watch'
len(data)

compressed
