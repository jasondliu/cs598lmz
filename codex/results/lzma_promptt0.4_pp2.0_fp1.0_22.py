import lzma
# Test LZMADecompressor.decompress()

compressed = b'x\x9cK\xcb\xcf\x07\x00\x02\xe5\x02\x00!\x01\x16\x00\x00\x00'

decomp = lzma.LZMADecompressor()

print(decomp.decompress(compressed))

# Test LZMADecompressor.decompress() with multiple calls

compressed = b'x\x9cK\xcb\xcf\x07\x00\x02\xe5\x02\x00!\x01\x16\x00\x00\x00'

decomp = lzma.LZMADecompressor()

print(decomp.decompress(compressed[:5]))
print(decomp.decompress(compressed[5:]))

# Test LZMADecompressor.decompress() with multiple calls
# and unconsumed data

compressed = b'x\x9cK\xcb\
