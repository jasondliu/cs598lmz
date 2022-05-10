import lzma
# Test LZMADecompressor.
c = lzma.LZMADecompressor()

with lzma.open("test.xz", "rb") as f:
    file_content = f.read()
    decompressed_data = c.decompress(file_content)

print(decompressed_data)

with open("test.txt", "wb") as f:
    f.write(decompressed_data)

# Test LZMACompressor.
c = lzma.LZMACompressor()

with open("test.txt", "rb") as f:
    file_content = f.read()
    compressed_data = c.compress(file_content)

print(compressed_data)

with open("test.xz", "wb") as f:
    f.write(compressed_data)
</code>

