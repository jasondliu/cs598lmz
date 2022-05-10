import lzma
# Test LZMADecompressor

with lzma.open('test.xz') as f:
    file_content = f.read()

print(file_content)

# Test LZMAEncoder

with lzma.open('test.xz', 'w') as f:
    f.write(b"Test")
    f.write(b"Test")
    f.write(b"Test")
    f.write(b"Test")

# Test LZMADecompressor

with lzma.open('test.xz') as f:
    file_content = f.read()

print(file_content)

# Test LZMAEncoder

with lzma.open('test.xz', 'w') as f:
    f.write(b"Test")
    f.write(b"Test")
    f.write(b"Test")
    f.write(b"Test")

# Test LZMADecompressor

with lzma.open('test.xz') as f:
    file_content = f.read
