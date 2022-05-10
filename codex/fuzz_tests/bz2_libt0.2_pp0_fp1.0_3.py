import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 可以看到，压缩和解压是一样的，速度非常快，而且压缩后的文件很小。
# bz2模块还提供了一个BZ2Compressor和BZ2Decompressor类，可以通过这两个类实现更底层的压缩和解压操作。
# 下面的例子演示了如何将一个大文件分块压缩，并保存为多个小文件：
import os
import
