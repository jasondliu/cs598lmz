from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# 使用 LZMADecompressor 类来构建一个解压器，可以重复使用解压器对数据进行多次解压。
# 解压器对象有一个 decompress() 方法，它接受一个单独的数据块并返回一个解压后的字符串。
# 如果解压后的数据不完整
