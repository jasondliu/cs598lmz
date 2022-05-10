from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

import zlib
zlib.decompress(data)

import bz2
bz2.decompress(data)

#%%
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

#zlib.crc32(s) #unsupported operation: crc32

#%%
import bz2
bz2.compress(s) 

bz2.decompress(t)

#%%
import zlib
import binascii

s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

binascii.hexlify(t)

#%%
import zlib
import binascii

binascii.crc32(s)

#%%
import struct
struct.pack('>I',10240099)


