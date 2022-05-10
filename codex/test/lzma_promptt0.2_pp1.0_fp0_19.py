import lzma
# Test LZMADecompressor

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read()
    result = decompressor.decompress(data)
    print(result)

# Test LZMADecompressor.decompress

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    result = decompressor.decompress(f.read())
    print(result)

# Test LZMADecompressor.decompress with max_length

with open('test.xz', 'rb') as f:
    decompressor = lzma.LZMADecompressor()
    result = decompressor.decompress(f.read(), max_length=10)
    print(result)

# Test LZMADecompressor.decompress with max_length and return_unconsumed_tail

