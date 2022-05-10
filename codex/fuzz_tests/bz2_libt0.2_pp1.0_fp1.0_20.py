import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 可以看到，压缩和解压是一样的，速度非常快，而且压缩后的文件很小。
# 但是，只能用于小文件，因为压缩/解压缩是一个内存密集型的过程。

# 压缩文件
# 压缩文件用的就是 bz2 模块里的压缩类，它们是 BZ2Compressor 和 BZ2Decompressor。
# 压缩文件
with bz2.BZ2File('test.bz2',
