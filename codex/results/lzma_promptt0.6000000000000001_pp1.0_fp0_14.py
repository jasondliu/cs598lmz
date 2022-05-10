import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
data = '7zXZ' + 'Y'*5 + 'X'*2 + 'Z'*6
print(decompressor.decompress(data))

# Test LZMADecompressor.decompress
decompressor = lzma.LZMADecompressor()
data = '7zXZ' + 'Y'*5 + 'X'*2 + 'Z'*6
print(decompressor.decompress(data))

# Test LZMADecompressor.flush
decompressor = lzma.LZMADecompressor()
data = '7zXZ' + 'Y'*5 + 'X'*2 + 'Z'*6
decompressor.decompress(data, max_length=3)
print(decompressor.decompress(b''))

# Test LZMADecompressor.decompress with max_length
decompressor = lzma.LZMADecompressor()
data =
