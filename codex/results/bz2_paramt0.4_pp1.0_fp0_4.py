from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world'))

# 使用compress()方法将数据压缩后，再使用decompress()方法解压缩。
# compress()方法返回的是一个bytes对象，可以将其写入文件或者使用其他方式传输。
# decompress()方法接受一个bytes对象并且返回一个原始字符串还原后的数据。
# 使用bz2模块压缩数据并将结果写入文件
import bz2
with open('bz2_compress.bz2', 'wb') as f:
    f.
