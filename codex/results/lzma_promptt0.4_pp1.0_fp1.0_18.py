import lzma
# Test LZMADecompressor

with lzma.open("test.xz", "rb") as f:
    file_content = f.read()

print(file_content)

# Test LZMACompressor

with lzma.open("test2.xz", "wb") as f:
    f.write(file_content)
