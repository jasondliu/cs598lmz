from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

# 设置压缩级别
compressor = BZ2Compressor(9)
compressor.compress(data)
compressor.flush()

# 压缩和解压文件
with BZ2File('data.bz2', 'w') as f:
    f.write(data)

with BZ2File('data.bz2', 'r') as f:
    f.read(100)
