from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

import lzma
lzma.decompress(xz_data)

# 在许多情况下，你需要将压缩的数据读到一个内存中的
# 切片（slice）中或者从一个文件中读取。为了支持这样的操作，
# 许多压缩库都提供了一个可以迭代产生原始未压缩数据块
# 的迭代器。比如，下面是如何对一个文件执行压缩和解压缩操
