import lzma
lzma.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# decompress() 函数可以处理原始的压缩数据和与 gzip 或者 bz2 模块相同的文件格式。
# 它还能识别文件头并智能选择合适的解压缩算法。

# 如果数据已经被压缩过了，那么可以使用 decompress() 函数来解压缩它。
#
