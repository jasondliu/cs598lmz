import lzma
lzma.decompress(lz_data)

#%%
# lzma
import lzma
import binascii
# lzma 压缩
lz_data = lzma.compress(b'hello,world!')
print(lz_data)
print(binascii.b2a_hex(lz_data))
# lzma 解压缩
print(lzma.decompress(lz_data))
#%%
# 压缩模块
import zlib
import binascii
# zlib 压缩
z_data = zlib.compress(b'hello,world!')
print(z_data)
print(binascii.b2a_hex(z_data))
# zlib 解压缩
print(zlib.decompress(z_data))
#%%
# 压缩模块
import bz2
import binascii
# bz2 压
