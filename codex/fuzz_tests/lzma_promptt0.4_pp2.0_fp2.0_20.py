import lzma
# Test LZMADecompressor with a file object
with open('test.lzma', 'rb') as f:
    decomp = lzma.LZMADecompressor()
    data = decomp.decompress(f.read())
    print(data)

# Test LZMADecompressor with a file object and a max_length argument
with open('test.lzma', 'rb') as f:
    decomp = lzma.LZMADecompressor()
    data = decomp.decompress(f.read(), max_length=100)
    print(data)

# Test LZMADecompressor with a file object and a max_length argument
with open('test.lzma', 'rb') as f:
    decomp = lzma.LZMADecompressor()
    data = decomp.decompress(f.read(), max_length=1000)
    print(data)

# Test LZMADecompressor with a file object and a max_length argument
with open('test.lzma', 'rb') as f:
    decomp = l
