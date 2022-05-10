import lzma
# Test LZMADecompressor
c = lzma.LZMADecompressor()
with open('compressed_data.xz', 'rb') as f:
    data = f.read()
    decompressed_data = c.decompress(data)
    print(decompressed_data)

# Test LZMACompressor
c = lzma.LZMACompressor()
with open('compressed_data.xz', 'wb') as f:
    f.write(c.compress(b'Hello World'))
    f.write(c.flush())

c = lzma.LZMACompressor(format=lzma.FORMAT_ALONE)
with open('compressed_data.xz', 'wb') as f:
    f.write(c.compress(b'Hello World'))
    f.write(c.flush())

# Test LZMAFile
with lzma.open('compressed_data.xz', 'rb') as f:
    print(f.read())

with lzma.open('compressed_data.
