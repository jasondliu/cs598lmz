from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 可以看到，这个数据被压缩过。
# 为了处理这种数据，可以使用 bz2 模块中的 BZ2Decompressor 类。
# 下面是一个例子：

# 读取压缩数据
with open('somefile.bz2', 'rb') as f:
    data = f.read()

# 创建一个解压器
decompressor = BZ2Decompressor()

# 一次处理一部分数据
for chunk in iter(lambda: decompressor.decompress(data), b''):
    process_data(chunk)

# 如果你想
