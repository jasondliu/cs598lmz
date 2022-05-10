import lzma
# Test LZMADecompressor.read()

# Basic test
dec = lzma.LZMADecompressor()
with open("lzma_data", "rb") as f:
    data = f.read()
out = dec.decompress(data)
print(out)

# Test read()
dec2 = lzma.LZMADecompressor()
with open("lzma_data", "rb") as f:
    data = f.read()
dec2.decompress(data[:5])
out = dec2.decompress(data[5:])
print(out)
