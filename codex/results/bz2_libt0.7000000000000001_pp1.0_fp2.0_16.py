import bz2
bz2.decompress(bz2_data)

# 可以看到，bz2 模块用于压缩和解压缩的类和函数都是小写的。而 zlib 模块则是大写的。

# 压缩
bz2_compressor = bz2.BZ2Compressor()
result = bz2_compressor.compress(data)
result += bz2_compressor.flush()

# 解压缩
bz2_decompressor = bz2.BZ2Decompressor()
original_data = bz2_decompressor.decompress(bz2_data)
original_data += bz2_decompressor.flush()
