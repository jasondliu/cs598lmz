from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# 如果输入是一个文件对象，则可以使用另外一个类 LZMAFile，它提供了一个类似于普通文件对象的接口。
# 对于普通的压缩，它会像下面这样工作：
with open('example.xz', 'rb') as input:
    with lzma.open(input) as decompressor:
        with open('uncompressed.txt', 'wb') as output:
            output.write(decompressor.read())
# 如果你想使用不同的压缩级别或者其他选项，可
