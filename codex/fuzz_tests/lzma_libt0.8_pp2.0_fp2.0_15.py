import lzma
lzma.decompress(lzma.compress(b"a"))

# 注意
# 如果检测到给定对象的接口与 zlib 接口相同，则从 zlib 模块
# 中导入 compress() 和 decompress() 函数到 lzma 中
# 否则，还是会从 lzma 模块中导入
# 这允许脚本编写同时支持 lzma 和 zlib
try:
    import zlib
    compression = zlib.compressobj(1)
    compress = compression.compress
    compress += compression.flush
except ImportError:
    compress = lzma.compress
compress(b"hello world!!!")
