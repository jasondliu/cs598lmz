import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对数据进行压缩和解压缩。
# 压缩后的数据就可以保存到文件或者通过网络传输了。

# 尽管 bz2 模块提供了一个压缩的基础接口，但是通常还是建议使用 zlib 模块来处理压缩数据。
# zlib 模块提供了更多的压缩级别
