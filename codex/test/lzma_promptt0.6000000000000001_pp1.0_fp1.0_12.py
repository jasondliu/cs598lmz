import lzma
# Test LZMADecompressor with a file
f = open('compressed.xz', 'rb')
decompressor = lzma.LZMADecompressor()
data = decompressor.decompress(f.read())
print(data)

# Test LZMADecompressor with multiple chunks
compressed = b'\xe5\x02\xf3\x48\xcd\xc9\xc9\x07\x00\x06\x04\x00\x02\xff\xff\xff\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
decompressor = lzma.LZMADecompressor()
