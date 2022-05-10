from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_compressed_data)

import lzma
with open('test.txt.xz', 'rb') as f:
    file_content = f.read()
file_content

lzma_compressed = lzma.compress(b'witch which has which witches wrist watch')
lzma_compressed

lzma.decompress(lzma_compressed)

import lzma
with lzma.open('test.txt.xz') as f:
    file_content = f.read()
file_content

import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

import zlib
ret = zlib.crc32(b'witch which has which witches wrist watch')
ret

ret = zlib.crc32(b'witch which has which witches wrist watch')
ret

ret = z
