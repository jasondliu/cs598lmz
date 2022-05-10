from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用bz2模块进行压缩和解压
import bz2
bz2.compress(data)
bz2.decompress(data)

# 使用zlib模块进行压缩和解压
import zlib
zlib.compress(data)
zlib.decompress(data)

# 使用brotli模块进行压缩和解压
import brotli
brotli.compress(data)
brotli.decompress(data)

# 使用lz4模块进行压缩和解压
import lz4
lz4.frame.compress(data)
lz4.frame.decompress(data)

# 使用zstandard模
