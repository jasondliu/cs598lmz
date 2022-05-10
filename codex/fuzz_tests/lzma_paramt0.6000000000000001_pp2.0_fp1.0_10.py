from lzma import LZMADecompressor
LZMADecompressor().decompress(lzma_data)

# 使用bz2压缩
import bz2
bz2_comp = bz2.BZ2Compressor()
bz2_data = bz2_comp.compress(raw_data)
bz2_data += bz2_comp.flush()
bz2_comp.decompress(bz2_data)
