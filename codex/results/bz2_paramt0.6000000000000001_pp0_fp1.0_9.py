from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(bytes("Hello World", "utf-8")))

# Python3 bz2 模块
# https://www.runoob.com/python3/python3-module-bz2.html

# bz2.compress(data, compresslevel=9)
# 参数
# data -- 压缩的数据
# compresslevel -- 压缩等级，默认为 9，最大为 9
# 返回值
# 返回压缩后的数据

# bz2.decompress(data)
# 参数
# data -- 解压缩的数据
# 返回值
# 返回解压缩后的数据

# BZ2File(filename[, mode[, compresslevel]]
