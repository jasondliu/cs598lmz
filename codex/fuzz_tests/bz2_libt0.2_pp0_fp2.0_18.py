import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# bz2.compress() 和 bz2.decompress() 函数分别对数据进行压缩和解压缩。
# 它们使用的是 bzip2 算法，它是一个可以提供比 gzip 更高压缩比的无损数据压缩算法。
# 压缩效率比 gzip 更高，但是压缩和解压缩速度比 gzip 慢。

# 如果需要对大量的数据进行压缩，比如
