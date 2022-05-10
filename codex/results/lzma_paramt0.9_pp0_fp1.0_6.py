from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# 高级功能
import bz2

compressor = bz2.BZ2Compressor()
print(compressor.compress(b'hello world'))
print(compressor.compress(b'hello world'))
print(compressor.flush())

# 变量-shelve
# shelve模块可以将程序内部的内置数据持久化的存储在一个外部的文件中
# import shelve
# s = shelve.open('shelf.dat')
# s['x'] = ['a', 'b', 'c']
# s['x'].append('d')
# s.close()
#
# # 打开文件时，给它一个模式
# # 缺省超写
# # 追加
