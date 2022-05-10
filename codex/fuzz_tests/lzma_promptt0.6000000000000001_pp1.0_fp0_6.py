import lzma
# Test LZMADecompressor

print("Testing LZMADecompressor")

# create compressor
compressor = lzma.LZMACompressor()

# compress data
data = b'The quick brown fox jumps over the lazy dog'
compressed = compressor.compress(data)
print("compressed is {} bytes".format(len(compressed)))

# create decompressor
decompressor = lzma.LZMADecompressor()

# decompress data
decompressed = decompressor.decompress(compressed)
print("decompressed is {} bytes".format(len(decompressed)))

# finished
print("Finished")
