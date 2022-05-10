import lzma
# Test LZMADecompressor

with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()

print(file_content)

# Test LZMACompressor

compressor = lzma.LZMACompressor()

