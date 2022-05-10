from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Compress data
compressor = LZMACompressor()
data = b'...'
more_data = b'...'
compressed = compressor.compress(data)
compressed += compressor.compress(more_data)
compressed += compressor.flush()
</code>

