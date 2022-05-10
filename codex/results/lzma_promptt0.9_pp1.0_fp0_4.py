import lzma
# Test LZMADecompressor work
d = lzma.LZMADecompressor()
decompressed = d.decompress(b'\x00\x00\x00\x00-\xac\x6cd\x00\x00\x00\x00\x05\x00\x00\x00\xf6')
print(decompressed)

# Sample output
# b'\x01'

# Test LZMA compress() function works
lzma_data = lzma.compress(b'\x01')

print(lzma_data)

# Sample output
# b'\x00\x00\x00\x00-\xac\x6cd\x00\x00\x00\x00\x05\x00\x00\x00\xf6'

# Test that LZMA decompressor works with compress()-generated data
d = lzma.LZMADecompressor()
decompressed = d.decompress(lzma_data)
print(decompressed)

# Sample output
