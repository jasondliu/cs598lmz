import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()
data = b'This is the original text.'
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test LZMADecompressor.decompress() with multiple calls

decompressor = lzma.LZMADecompressor()
decompressed = b''
