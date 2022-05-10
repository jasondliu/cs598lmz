import bz2
bz2.compress(b'hello world')

#
# 使用 bz2 模块压缩数据，然后使用起来和一般的文件一样。
#
# 比如，和 gzip 模块类似，bz2 模块提供 compress() 和 decompress() 函数。和 gzip 模块不同的是，bz2 模块没有 open() 函数，而是直接使用 BZ2File() 函数。
#
# bz2.compress(data) # 压缩数据
# bz2.decompress(data) # 解压缩数据
#
# BZ2File(filename, mode='
