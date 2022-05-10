import lzma
# Test LZMADecompressor

data = lzma.compress(b"Hello World!")

decomp = lzma.LZMADecompressor()
result = decomp.decompress(data)

print(result.decode())

# Test LZMAFile

