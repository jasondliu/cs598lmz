import lzma
# Test LZMADecompressor

with lzma.open('test.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMACompressor

compressor = lzma.LZMACompressor()
with open('test.xz', 'wb') as f:
    f.write(compressor.compress(b'Hello'))
    f.write(compressor.compress(b'World!'))
    f.write(compressor.flush())

# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()
with open('test.xz', 'rb') as f:
    file_content = decompressor.decompress(f.read())
    print(file_content)

# Test LZMAFile

with lzma.open('test.xz') as f:
    file_content = f.read()
    print(file_content)

# Test LZMAFile

