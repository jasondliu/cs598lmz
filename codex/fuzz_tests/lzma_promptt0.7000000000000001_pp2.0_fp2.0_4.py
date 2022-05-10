import lzma
# Test LZMADecompressor with a small data.
compressor = lzma.LZMACompressor()
data = b'this is the original, uncompressed data'
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
result = decompressor.decompress(compressed)
result += decompressor.flush()
result

# Test the .copy() method.
import io
import lzma
data = b'this is the original, uncompressed data'
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor1 = lzma.LZMADecompressor()
result = decompressor1.decompress(compressed)
result += decompressor1.flush()
result
decompressor2 = lzma.LZMADecompressor()
decompressor1.copy()
result = decompressor2.decompress(compressed)
result += decompressor2.flush()
result

# Test the
