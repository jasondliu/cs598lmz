from lzma import LZMADecompressor
LZMADecompressor().decompress(z)

#%%
# simple compression
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

#%%
# more compression
import zlib
import binascii

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

binascii.crc32(s)

zlib.crc32(s)

#%%
# bzip2 compression
import bz2

t = bz2.compress(s)
len(t)

bz2.decompress(t)

bz2.crc32(s)

#%%
# lzma compression
import lzma

t = lzma.compress(s)
len(t)

lzma.decompress(t)
