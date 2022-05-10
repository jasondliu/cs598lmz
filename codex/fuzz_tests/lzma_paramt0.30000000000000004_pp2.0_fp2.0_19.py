from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用lzma模块压缩和解压缩文件
# 压缩文件
import lzma
with lzma.open('somefile.xz', 'wt') as f:
    f.write(text)

# 解压缩文件
import lzma
with lzma.open('somefile.xz') as f:
    text = f.read()

# 使用bz2模块压缩和解压缩数据
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)

# 使用bz2模块压缩和
