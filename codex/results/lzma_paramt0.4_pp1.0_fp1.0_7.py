from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!'

# 如果数据压缩的时候没有提供一个有效的数据校验值，则可以设置 check 参数来指定校验类型
decompressor = LZMADecompressor()
decompressor.decompress(data, check=-1)

# b'Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!'

# 如果数据被压缩的时候使用了一个支持的校验类型
