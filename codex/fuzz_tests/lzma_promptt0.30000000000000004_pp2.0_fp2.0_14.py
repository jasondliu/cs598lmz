import lzma
# Test LZMADecompressor
with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with decompressor.stream(f) as d:
        with open('test.txt', 'wb') as f:
            f.write(d.read())
# Test LZMADecompressor.decompress
with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('test.txt', 'wb') as f:
        f.write(decompressor.decompress(f.read()))
# Test LZMADecompressor.flush
with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    with open('test.txt', 'wb') as f:
        f.write(decompressor.flush())
# Test LZMADecompressor.unused_data
with open('test.xz', 'rb') as f:
    decompressor =
