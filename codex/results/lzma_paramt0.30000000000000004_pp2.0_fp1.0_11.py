from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 这个例子展示了如何使用 LZMADecompressor 对象来解压缩数据。
# 它的使用方法与 zlib.decompress() 和 bz2.decompress() 类似。
# 如果要解压缩的数据不是一个完整的压缩文件，那么需要使用 decompress() 方法的 max_length 参数来限制解压缩后的
