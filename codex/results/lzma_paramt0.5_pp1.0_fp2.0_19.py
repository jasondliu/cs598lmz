from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# compress
from lzma import LZMACompressor
LZMACompressor().compress(data)

# compress w/ filter
from lzma import LZMACompressor
compressor = LZMACompressor(
    filters=[
        {"id": LZMA_FILTER_LZMA2, "preset": 0 | LZMA_PRESET_EXTREME},
    ],
)
LZMACompressor().compress(data)

# compress w/ filter
from lzma import LZMACompressor
compressor = LZMACompressor(
    filters=[
        {"id": LZMA_FILTER_X86, "preset": 0 | LZMA_PRESET_EXTREME},
        {"id": LZMA_FILTER_X86, "preset": 0 | LZMA_PRESET_EXTREME},
    ],
)
LZMACompressor().compress(data)


# compress w/ filter
from lzma import LZMACompressor
compressor = LZMAComp
