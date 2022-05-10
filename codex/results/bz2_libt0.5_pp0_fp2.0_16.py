import bz2
bz2.decompress(bz2.compress(b"hello world"))

# bz2.compress() 和 bz2.decompress() 函数分别接受一个 bytes 对象作为输入并返回一个 bytes 对象作为输出。 它们不能处理 Unicode 字符串，只能处理二进制数据。

# 如果你想处理文本数据，你需要使用 Unicode 字符串并在进行解码和编码操作时进行相应的转换。

# 内置的 gzip 和 bz2 模
