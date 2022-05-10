from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.open
# bz2.open(filename, mode='r', compresslevel=9, encoding=None, errors=None, newline=None)
# 以指定的压缩级别（0-9）打开一个文件，返回一个 BZ2File 对象

# bz2.BZ2File
# bz2.BZ2File(filename, mode='r', compresslevel=9, encoding=None, errors=None, newline=None)
# 以指定的压缩级别（0-9）打开一个文件，返回一个 BZ2File 对象
# BZ2File 对象与普通文件对象类似，支
