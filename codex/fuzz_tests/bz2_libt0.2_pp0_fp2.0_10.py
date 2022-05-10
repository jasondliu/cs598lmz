import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 标准库提供了一个 bz2 模块来支持 bzip2 算法压缩和解压缩，它的压缩效率比 gzip 模块高很多，但是它的速度比 gzip 模块慢很多。
# 如果需要解压缩的文件很大，或者是需要多次解压缩，使用 bz2 模块会更好。

# 小结
# 压缩和解压缩是非常
