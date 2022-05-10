from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 更多关于压缩数据的信息，参考6.17小节

# 6.8 在字节串上执行其他的文本操作(text operations)
# 你想在字节串上执行一些简单的文本操作，比如移除，搜索和替换
data = b'Hello World'
data[0:5]
# b'Hello'
data.startswith(b'Hello')
# True
data.split()
# [b'Hello', b'World']
data.replace(b'Hello', b'Hello Cruel')
# b'Hello Cruel World'
# 相关的操作还有endswith(), r
