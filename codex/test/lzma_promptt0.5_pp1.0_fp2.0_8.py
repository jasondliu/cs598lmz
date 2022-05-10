import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
try:
    compressor.compress(b"some data")
except Exception as e:
    print(e)

# Test LZMADecompressor
data = b"test"
compressor = lzma.LZMACompressor()
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
try:
    decompressed = decompressor.decompress(compressed)
except Exception as e:
    print(e)
