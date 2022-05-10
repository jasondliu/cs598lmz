import bz2
bz2.compress('abc')

# 使用bz2.BZ2Compressor对象进行压缩
bz2.BZ2Compressor().compress('abc')

# 使用bz2.BZ2Compressor对象进行压缩
compressor = bz2.BZ2Compressor()
compressor.compress('abc')
compressor.compress('123')
compressor.flush()

# bz2.BZ2Decompressor对象使用
bz2.BZ2Decompressor().decompress(compressed)

# 使用with子句进行压缩和解压
compressed = bz2.compress('abc')
with bz2.BZ2File('compress.bz2', 'w') as output:
    output.write(compressed)

with bz2.BZ2File('compress.bz2', 'r
