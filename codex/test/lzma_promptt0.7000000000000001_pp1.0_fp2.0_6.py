import lzma
# Test LZMADecompressor.decompress()

# Test decompression algorithm and defaults
dec = lzma.LZMADecompressor()
indata = b'1234567890' * 1000000
