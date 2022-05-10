from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.open()
with bz2.open('example.bz2', 'rt') as input:
    print(input.read())

with bz2.open('example.bz2', 'wt') as output:
    output.write('Contents go here.')

# zlib.compress()
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# zlib.compress()
import binascii
binascii.crc32(s)

# zlib.compress()
import zlib
import binascii

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

binascii
