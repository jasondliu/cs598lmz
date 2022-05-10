import lzma
# Test LZMADecompressor
lzmaDecompressor = lzma.LZMADecompressor()
print(lzmaDecompressor.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00'))

# Test LZMADecompressor with filters
lzmaDecompressor = lzma.LZMADecompressor(lzma.FORMAT_XZ, filters=[
    {
        "id": lzma.FILTER_LZMA2,
        "preset": lzma.PRESET_EXTREME
    }
])

print(lzmaDecompressor.decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00'))

# Compress a string
compressed = lzma.compress(b'Hello World')
print
