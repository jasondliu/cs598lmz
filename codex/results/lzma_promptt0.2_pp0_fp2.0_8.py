import lzma
# Test LZMADecompressor

with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()

print(file_content)

# Test LZMACompressor

with lzma.open('test.xz', 'wb') as f:
    f.write(b"Hello World!")

# Test LZMADecompressor

with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()

print(file_content)

# Test LZMACompressor

with lzma.open('test.xz', 'wb') as f:
    f.write(b"Hello World!")

# Test LZMADecompressor

with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()

print(file_content)

# Test LZMACompressor

with lzma.open('test.xz', 'wb') as f:
    f.write(b"Hello
