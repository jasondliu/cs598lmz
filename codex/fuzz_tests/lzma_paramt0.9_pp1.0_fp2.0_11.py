from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
from bz2 import decompress
decompress(data)
from zlib import decompress, MAX_WBITS
decompress(data, -MAX_WBITS)

# 压缩数据
from zlib import compressobj
co = compressobj(level=6, method=DEFLATED, wbits=MAX_WBITS, memLevel=8, strategy=Z_DEFAULT_STRATEGY)
data = co.compress(data)
data += co.flush()
import lzma
lzc = lzma.LZMACompressor()
data = lzc.compress(data)
data += lzc.flush()
import bz2
compressor = bz2.BZ2Compressor()
data = compressor.compress(data)
data += compressor.flush()
