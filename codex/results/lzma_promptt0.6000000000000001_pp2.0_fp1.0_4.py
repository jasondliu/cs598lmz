import lzma
# Test LZMADecompressor

# Create a decompressor object
decompressor = lzma.LZMADecompressor()

# Read one byte, will return empty bytes object on EOF
print(decompressor.decompress(b'X'))

# Read all available data
print(decompressor.decompress(b'BZh91AY&SY'))

# Read some more data
print(decompressor.decompress(b'A\xc8\x00\x00W\x18\x00\x08\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
