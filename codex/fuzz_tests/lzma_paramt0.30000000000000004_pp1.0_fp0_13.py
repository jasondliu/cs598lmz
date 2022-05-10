from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 这个类支持流式解压缩，使用方法如下：
decompressor = LZMADecompressor()
with open('somefile.xz', 'rb') as input, open('somefile', 'wb') as output:
    for block in iter(lambda: input.read(1024 * 1024), b''):
        output.write(decompressor.decompress(block))

# 如果要解压缩一个已知大小的数据块，可以使用decompress()方法。
# 下面是一个简单的例子：
data = open('somefile.xz', 'rb').read()
decompressor = LZMADecompressor()
result = decompressor.decompress(data)

#
