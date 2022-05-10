import bz2
bz2.decompress(data)

# 使用bz2.BZ2Decompressor来创建一个解压对象
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)
# decompressor.decompress(data)

# 可以使用incremental()方法来读取内容
decompressor.decompress(data[:100])
decompressor.decompress(data[100:])

# 可以使用incremental()方法来读取内容
decompressor.decompress(data[:100])
decompressor.decompress(data[100:])

# 可以使用incremental()方法来读取内容
decompressor.decompress(data[:100])
decompressor.decompress(data[100:])

# 可以
