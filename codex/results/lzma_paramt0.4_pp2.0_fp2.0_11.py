from lzma import LZMADecompressor
LZMADecompressor().decompress(b'...')

# 可以通过设置 format 参数来指定输出的格式，如果没有指定，则返回原始的二进制字节。
# 还可以设置 check 参数来指定校验和类型。
# 如果指定了 check 参数，校验和检查失败会引发 LZMAError 异常。
# 如果不指定 check 参数，校验和检查失败会返回 None。
# 校验
