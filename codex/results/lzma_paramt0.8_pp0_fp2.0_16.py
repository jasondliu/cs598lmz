from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed)

# 可以查看源代码中的 _LZMACompressor 中有进行压缩的方法

# 使用 LZMADecompressor 对象需要注意的是源数据必须包含完整的 LZMA 编码的数据块
# 否则会抛出 EOFError

# compress() 函数使用了默认的压缩等级 6。
# 可以通过创建一个 LZMACompressor 对象来指定不同的压缩等级
# 压缩等级可视为 0-9 之间的
