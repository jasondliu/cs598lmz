import lzma
lzma.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# 对于普通文件，使用xz压缩比gz压缩更小。
# lzma模块主要用来压缩数据，但是提供了一个使用LZMA算法解压数据的类LZMADecompressor。
# 它使用一个非常类似于bz2模块中的BZ2Decompressor类。
import lzma
with open('lzma_compress.
