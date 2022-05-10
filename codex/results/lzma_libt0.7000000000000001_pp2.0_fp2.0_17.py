import lzma
lzma.open('sample.data')

# lzma 模块的 compress 函数也可以将一个字节序列进行压缩。
import lzma
data = b'this is the data to compress'
compressed = lzma.compress(data)
print(compressed)

# lzma 模块除了支持文件对象外，还支持使用缓存来直接压缩和解压数据，如下所示。
import lzma
data = b'this is the data to compress'
compressed = lzma.compress(data)
print(compressed)

# decompress 函数可以解压之前压缩的数据。
import
