import lzma
# Test LZMADecompressor
with open('data/lzma.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    decompressed_data = decompressor.decompress(f.read())
    print(decompressed_data)

# Test LZMADecompressor with multiple chunks
with open('data/lzma.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    first_chunk = f.read(32)
    second_chunk = f.read()
    decompressed_data = decompressor.decompress(first_chunk)
    decompressed_data += decompressor.decompress(second_chunk)
    print(decompressed_data)

# Test LZMADecompressor with multiple chunks
with open('data/lzma.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    first_chunk = f.read(32)
    second_chunk =
