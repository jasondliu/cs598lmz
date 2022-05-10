import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor(
        filters=[
            {"id": lzma.FILTER_LZMA2,
             "preset": 9 | lzma.PRESET_EXTREME},
        ])

decompressor = lzma.LZMADecompressor()

