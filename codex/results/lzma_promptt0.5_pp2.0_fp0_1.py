import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()

with open('/home/gabriel/Desktop/lzma_compressed_file.txt', 'rb') as f:
    data = f.read()

decompressed_data = decompressor.decompress(data)
print(decompressed_data)

# Test LZMACompressor.
compressor = lzma.LZMACompressor()
compressed_data = compressor.compress(b"data")
compressed_data += compressor.flush()
print(compressed_data)

# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()
decompressed_data = decompressor.decompress(compressed_data)
print(decompressed_data)

# Test LZMAFile.
with lzma.open('/home/gabriel/Desktop/lzma_compressed_file.txt', 'rb') as f:
    content = f.read()
print(content)
