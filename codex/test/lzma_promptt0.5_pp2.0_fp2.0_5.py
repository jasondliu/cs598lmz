import lzma
# Test LZMADecompressor

# Test that the decompressor accepts empty data
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'')

# Test that the decompressor accepts a single byte
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00')

# Test that the decompressor accepts a single byte
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00' * 1000000)

# Test that the decompressor accepts a single byte
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00' * 1000000 + b'\xFF')

# Test that the decompressor accepts a single byte
decompressor = lzma.LZMADecompressor()
decompressor.decompress(b'\x00' * 1000000 + b'\xFF' * 1000000)
