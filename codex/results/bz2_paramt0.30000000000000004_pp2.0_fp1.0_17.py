from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

import lzma
lzma.decompress(lzma_data)

import zlib
zlib.decompress(zlib_data)

# 如果你想构建一个支持多种压缩格式的通用工具，可以使用 zlib 模块中的
# decompressobj() 函数来创建解压对象。比如：

decompressor = zlib.decompressobj()
decompressor.decompress(zlib_data)

# 如果你想控制压缩级别或其他选项，可以使用 compress() 和 decompress()
# 函数。比如
