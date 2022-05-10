import bz2
bz2.decompress(bz2.compress(b'hello world'))

# bz2.compress() 和 bz2.decompress() 函数分别对应于 bz2.BZ2Compressor 和 bz2.BZ2Decompressor 类。
# 如果你想控制压缩级别或者一次处理大量的数据，那么可以使用这些类。例如：

import bz2
compressor = bz2.BZ2Compressor(9)
compressor.compress(b'hello world!')
compressor.flush()

# 压缩级别是一个从 1 到 9 的整数，数字越大，压缩算法的
