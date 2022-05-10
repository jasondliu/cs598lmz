import bz2
bz2.decompress(bz2_data)

# 使用bz2模块进行数据压缩
data = b'ABC' * 1000000
len(data)
bz2_data = bz2.compress(data)
len(bz2_data)
bz2.decompress(bz2_data)

# 使用zlib模块进行数据压缩
import zlib
data = b'ABC' * 1000000
len(data)
zlib_data = zlib.compress(data)
len(zlib_data)
zlib.decompress(zlib_data)

# 使用lzma模块进行数据压缩
import lzma
data = b'ABC' * 1000000
len(data)
lzma_data = lzma.compress(data)
len(lzma_data)

