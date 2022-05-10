import bz2
bz2.decompress(bz2.compress(data)) == data

# bz2.compress() 方法用于压缩给定的数据，如果指定了 compresslevel，则使用指定的压缩级别。
# 压缩级别默认为 9，最高压缩率。
# bz2.decompress() 方法用于解压缩，它只接受一个参数，即需要解压的数据。

# 压缩
data = b'Lots of data here.'
len(data)

compressed = bz2.compress(data)
len(compressed)

# 解压缩
decomp
