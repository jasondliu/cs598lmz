from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'Hello World'))

# bz2.open()
with bz2.open('file.bz2', 'wt') as f:
    f.write('Hello World')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# zlib.compress()
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# zlib.compress()
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# zlib.compress()
import zlib
s = b'witch which has which witches wrist watch'
len(s)
