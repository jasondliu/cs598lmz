import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with open('test.xz', 'rb') as f:
    data = f.read()
    print(decompressor.decompress(data))

# Test LZMACompressor

compressor = lzma.LZMACompressor()

with open('test.xz', 'wb') as f:
    f.write(compressor.compress(b'Hello world!'))
    f.write(compressor.flush())

# Test open()

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

with lzma.open('test.xz', 'wb') as f:
    f.write(b'Hello world!')

# Test LZMAFile

with lzma.open('test.xz', 'rb') as f:
    print(f.read())

