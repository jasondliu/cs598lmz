import lzma
# Test LZMADecompressor
c = lzma.LZMADecompressor()
with open('lzma_file.xz', 'rb') as f:
    file_content = f.read()
file_content = c.decompress(file_content)
print(file_content)

# Test LZMACompressor
c = lzma.LZMACompressor()
with open('lzma_file.xz', 'wb') as f:
    f.write(c.compress(file_content))
    f.write(c.flush())

# Test open
with lzma.open('lzma_file.xz') as f:
    file_content = f.read()
print(file_content)

# Test compress
compressed = lzma.compress(file_content)
print(compressed)

# Test decompress
decompressed = lzma.decompress(compressed)
print(decompressed)
