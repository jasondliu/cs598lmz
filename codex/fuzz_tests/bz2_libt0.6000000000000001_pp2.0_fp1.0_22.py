import bz2
bz2.decompress(data)

# 此外还有lzma
import lzma
lzma.decompress(data)

# 要进行bz2或者lzma压缩，先得到一个压缩对象
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# 对于lzma压缩，你可以指定级别
import lzma
compressor = lzma.LZMACompressor(format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=9)
compressor.compress(data)
compressor.flush()

# 解压缩
import bz2
decompressor = bz2.BZ2Decompressor()
decompressor.decompress
