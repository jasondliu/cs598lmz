import lzma
# Test LZMADecompressor object
lzc1 = lzma.LZMADecompressor()
print(lzc1.decompress(s).decode('utf-8'))
print(lzc1.decompress(s))

# Test LZMADecompressor with multiple calls to decompress
lzc2 = lzma.LZMADecompressor()
d = lzc2.decompress(s[:4])
d += lzc2.decompress(s[4:])
print(d.decode('utf-8'))

# Test max_length parameter
lzc3 = lzma.LZMADecompressor()
print(lzc3.decompress(s, max_length=20))

# Test different input types
lzc4 = lzma.LZMADecompressor()
print(lzc4.decompress(bytes(s)))
print(lzc4.decompress(bytearray(s)))
print(lzc4.decompress(memory
