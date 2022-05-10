import lzma
# Test LZMADecompressor

compressed = b"x\x9c\xab\x36\x0e\x00\x00\x10\x00\xff\xff"

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

# Check that the decompressor finished successfully.
decompressor.decompress(b"", True)

# The decompressor object provides information about the
# decompressed data.
decompressor.unused_data
# Test LZMACompressor

compressor = lzma.LZMACompressor()
compressor.compress(b"hello")

compressor.flush()
# Test LZMACompressor with filters

compressor = lzma.LZMACompressor(filters=[
    {"id": lzma.FILTER_ARM},
    {"id": lzma.FILTER_ARMTHUMB},
    {"id": lzma.FILTER_DELTA, "dist": 16},
    {"id": lzma.FILTER_LZMA
