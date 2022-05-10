import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00')

# Test LZMADecompressor with max_length
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00', max_length=1)

# Test LZMADecompressor with max_length and unconsumed_tail
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\xfd7z
