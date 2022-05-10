import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# bz2.compress() 和 bz2.decompress() 函数分别对数据进行压缩和解压缩。
# 它们只接受单个参数，即需要压缩或解压缩的数据。
# 压缩后的数据可以保存到一个文件或者使用其他的方式进行传输。
# 如果要按块的方式处理大量的数据，建议使用 BZ2File 对象。

# 压缩文件

