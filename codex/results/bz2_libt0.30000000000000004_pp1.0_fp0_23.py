import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 可以看到，压缩和解压是一样的，速度非常快，而且压缩后的文件很小。
#
# 我们在文件中读写时，就可以先压缩再写入，或者先从文件读取后解压缩，因为它们都是可以迭代的。
#
# bz2.compress() 和 bz2.decompress() 只接受 bytes 类型，str 类型需要先编码为 bytes，
# 示
