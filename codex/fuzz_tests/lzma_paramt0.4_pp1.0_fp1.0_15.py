from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 使用更多的内存来获得更好的压缩率
compressor = LZMACompressor(format=FORMAT_RAW, check=-1, preset=9 | LZMA_PRESET_EXTREME)
compressor.compress(b"some data")
compressor.flush()

# 压缩比高达2.3:1
compressor = LZMACompressor(format=FORMAT_XZ, check=CHECK_CRC64, preset=9 | LZMA_PRESET_EXTREME)
compressor.compress(b"some data")
compressor.flush()

# 压缩比高达2.3:1
compressor = LZMACompressor(format=FORMAT_ALONE, check=CHECK_CRC64, preset=9 | LZMA_PRESET_EXTREME)
compressor.compress(b"some data")
compressor
