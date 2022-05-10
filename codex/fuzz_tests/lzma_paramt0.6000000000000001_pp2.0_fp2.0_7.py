from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# 用不同的算法压缩
# 压缩算法可以通过 compresslevel 参数控制。
# 对于 LZMA 压缩来说，有 3 个级别可用，分别为 0，1，2。0 表示最快速度，2 表示最佳压缩率。
# 对于 bz2 来说，有 9 个级别可用，分别为 1 到 9。1 表示最快速度，9 表示最佳压缩率。
# 默认的压
