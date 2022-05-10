from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xe0\x01\xa9\x04\xfc\xb5\x1f\x00\x00')

# https://github.com/python/cpython/blob/master/Lib/lzma.py
# 下面哪行是错的？
# A. LZMACompressor().compress(b'x' * 100)
# B. LZMADecompressor().decompress(b'x' * 100)
# C. LZMADecompressor().decompress(b'\xe0\x01\xa9\x04\xfc\xb5\x1f\x00\x00')
# D. LZMACompressor().compress(b'\xe0\x01\xa9\x04\xfc\xb5\x1f\x00\x00')
# 参考资料：https://github.com/python/cpython/blob/master/Modules/_lzmamod
