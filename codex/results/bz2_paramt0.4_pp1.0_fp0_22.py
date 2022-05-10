from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.open(filename, mode='r', compresslevel=9, encoding=None, errors=None, newline=None)
# 打开一个bz2文件，返回一个文件对象
# 参数：
# filename：文件名
# mode：打开模式，默认是只读模式
# compresslevel：压缩级别，默认是9

# bz2.BZ2File(filename, mode='r', buffering=None, compresslevel=9, encoding=None, errors=None, newline=None)
# 以BZ2File对象的形式打开一个bz2文件
# 参数：
# filename：文件名
