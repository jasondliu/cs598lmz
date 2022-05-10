import bz2
bz2.decompress(data)

# bz2模块压缩数据
import bz2
bz2.compress(data)

# 函数实现压缩和解压
def bz2_compress(data):
    return bz2.compress(data)

def bz2_decompress(data):
    return bz2.decompress(data)

# 实例化压缩和解压类
bz2_en = BZ2Compressor()
bz2_de = BZ2Decompressor()

bz2_en.compress(data)
bz2_de.decompress(data)

# 实例化自定义过滤器
bz2_en = BZ2Compressor()
bz2_de = BZ2Decompressor()

#
