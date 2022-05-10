import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor(lzma.FORMAT_ALONE)
decompressor = lzma.LZMADecompressor(lzma.FORMAT_ALONE)

data = b'data to compress'
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressed = decompressor.decompress(compressed)
assert decompressed == data

