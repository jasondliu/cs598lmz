import lzma
# Test LZMADecompressor class
data = b"---x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x07\x81\x08 \x04"
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data)
decompressor.decompress(b"")

# Test LZMADecompressor.decompress(max_length=-1)
decompressor = lzma.LZMADecompressor()
decompressor.decompress(data, max_length=-1)

# Test decompressor initialization with LZMA_CONCATENATED preset.
data += b"--x\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00\x07\x81\x08 \x04"
decompressor = lzma.LZMADecompressor(lzma.FORMAT_RAW, None, lzma.PRESET_DE
