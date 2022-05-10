from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 还可以使用压缩数据的格式，以便得到更好的压缩效果。比如，使用xz格式：
data = b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00'
len(data)

LZMADecompressor().decompress(data)

# 如果你想压缩的数据有多个部分，可以多次调用decompress()方法

decompressor = LZMADecompressor()
decompressor.decompress(data)
