from lzma import LZMADecompressor
LZMADecompressor.decompress(lzma_data)

# Compress with LZMA
from lzma import LZMACompressor
lzma_compressor = LZMACompressor()
lzma_data = lzma_compressor.compress(b'This is a test')
lzma_data += lzma_compressor.flush()

# Compress with LZMA and a specified preset
from lzma import LZMACompressor
lzma_compressor = LZMACompressor(preset=9)
lzma_data = lzma_compressor.compress(b'This is a test')
lzma_data += lzma_compressor.flush()

# Compress with LZMA and a specified preset and a filter chain
from lzma import LZMACompressor
lzma_compressor = LZMACompressor(preset=9, filters={
    'id': lzma.FILTER_LZMA2,
    'dict_size': 2 ** 32,
    'lc': 3,
    'lp
