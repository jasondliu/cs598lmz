import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对数据进行压缩和解压缩。
# 压缩后的数据就可以保存到文件或者通过网络传输了。

# 如果要更加高效的支持大量的数据的压缩，可以使用 BZ2File 对象来代替 compress() 和 decompress() 函数。
# BZ2File 对象使用一个类似于普通文件对象的接口
