import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.decompress
decomp = lzma.LZMADecompressor()
data = b'\x5d\x00\x00\xff\xff\x03\x00\x04\x00\x04\x00\x00\x00'
print(decomp.decompress(data))

# Test LZMAEncoder
# https://docs.python.org/3/library/lzma.html#lzma.LZMAEncoder
with open('test.txt', 'rb') as f:
    data = f.read()
encoded = lzma.LZMAEncoder(preset=9).encode(data)
with open('test.lzma', 'wb') as f:
    f.write(encoded)

# Test LZMADecoder
# https://docs.python.org/3/library/lzma.html#lzma.LZMADecoder
