import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对数据进行压缩和解压缩。
# 压缩后的数据就可以保存到文件或者通过网络传输了。

# 小结
# 压缩和解压缩对于很多应用程序来说都是必须的，尤其是需要传输或者保存大量数据的时候。
# 压缩之后的数据可以降低磁盘
