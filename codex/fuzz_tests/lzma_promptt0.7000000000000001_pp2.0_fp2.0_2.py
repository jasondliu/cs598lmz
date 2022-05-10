import lzma
# Test LZMADecompressor by decompressing the data from its own compressed
# output.
compressor = lzma.LZMACompressor()
data = b'The quick brown fox jumps over the lazy dog'
compressed = compressor.compress(data)
compressed += compressor.flush()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
decompressed += decompressor.unconsumed_tail
print(decompressed)

# Test LZMADecompressor with an actual .xz file containing a short
# bytestring.
with open('lzma_compressed_data.xz', 'rb') as f:
    file_content = f.read()
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(file_content)
decompressed += decompressor.unconsumed_tail
print(decompressed)

# Test the incremental decompressor.
decompressor = lzma.LZMADecompressor()
decompressed =
