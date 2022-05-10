import lzma
# Test LZMADecompressor
compressor = lzma.LZMACompressor()
data = b'This is the original text.'
compressed = compressor.compress(data)
compressed += compressor.flush()
print(compressed)

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

