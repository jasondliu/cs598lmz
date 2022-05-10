from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Compress data
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b"some data")
compressor.flush()

# Compress data using a preset
from lzma import LZMACompressor
compressor = LZMACompressor(preset=9 | lzma.PRESET_EXTREME)
compressor.compress(b"some data")
compressor.flush()

# Compress data using a filter chain
from lzma import LZMACompressor
compressor = LZMACompressor(filters=[
    {"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME},
    {"id": lzma.FILTER_DELTA, "dist": 5},
])
compressor.compress(b"some data")
compressor.flush()

# Decompress data with a preset
from lzma import LZMADecompressor
decompressor = LZM
