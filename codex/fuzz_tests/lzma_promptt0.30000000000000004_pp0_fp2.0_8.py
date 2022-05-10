import lzma
# Test LZMADecompressor
with lzma.open('test.xz', 'rb') as f:
    file_content = f.read()
    print(file_content)

# Test LZMACompressor
compressor = lzma.LZMACompressor()
with open('test.xz', 'wb') as f:
    f.write(compressor.compress(b"Hello world!\n"))
    f.write(compressor.compress(b"Hello world!\n"))
    f.write(compressor.compress(b"Hello world!\n"))
    f.write(compressor.flush())

# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
with open('test.xz', 'rb') as f:
    file_content = f.read(100)
    print(decompressor.decompress(file_content))
    print(decompressor.decompress(file_content))
    print(decompressor.decompress(file_content))
    print(decompressor
