import bz2
bz2.decompress(bz2.compress(b'Hello World'))

# 可以看到，压缩和解压是一样的，在Python中，当我们写入bytes时，就表示占用的空间大小，如果写入的不是bytes，那么就会报错。
# 所以，这种压缩算法压缩后的数据其实比原数据还大，因为压缩算法是在内存中完成的，压缩后的数据是一个bytes类型。

# 我们很
