import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 可以看到，压缩和解压是一样的，速度非常快，而且压缩后的文件很小。
# bz2模块还提供了一个BZ2Compressor类和BZ2Decompressor类，可以通过这两个类实现更底层的控制。
# 下面的代码演示了如何压缩和解压一个大文件：

import bz2

with open('lorem.txt', 'rb') as input:
    with bz2.BZ2File
