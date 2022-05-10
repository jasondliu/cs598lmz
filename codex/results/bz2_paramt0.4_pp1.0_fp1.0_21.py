from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

#%%
s = "hello world!hello world!hello world!hello world!"
len(s)

#%%
import zlib
t = zlib.compress(s)
len(t)

#%%
zlib.decompress(t)

#%%
zlib.crc32(s)

#%%
zlib.crc32(s, 0)

#%%
zlib.crc32(s, zlib.crc32(s))

#%%
zlib.crc32(s, zlib.crc32(s)) & 0xffffffff

#%%
zlib.crc32(s, zlib.crc32(s)) & 0xffffffff == zlib.crc32(s + s) & 0xffffffff

#%%
import binascii
binascii.crc32(s)

#%%
binascii.crc32(s, 0)

#%%
binascii.crc32(s, binascii
