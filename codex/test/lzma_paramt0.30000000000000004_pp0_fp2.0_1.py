from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 这个例子中，我们使用了 LZMADecompressor 类来创建一个解压对象，然后使用它的 decompress() 方法来解压数据。
# 如果你想解压的数据是一个文件，那么你可以使用 lzma 模块提供的 open() 函数。比如：

