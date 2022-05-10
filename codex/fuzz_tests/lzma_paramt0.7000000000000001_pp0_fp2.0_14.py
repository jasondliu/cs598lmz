from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# If the compressed data is perfectly compressible, the compression
# ratio will be near 1000.

compressor = LZMACompressor()
compressor.compress(b'Binary data. ' * 1000)
compressed_data = compressor.flush()

len(b'Binary data. ' * 1000) / len(compressed_data)
