import lzma
# Test LZMADecompressor.__init__
try:
    lzma.LZMADecompressor(preset=1000)
except ValueError:
    pass
else:
    print('Failed')

# Test LZMADecompressor.decompress()
try:
    lzma.LZMADecompressor().decompress(b'\x00')
except ValueError:
    pass
else:
    print('Failed')

# Test LZMADecompressor.decompress()
try:
    lzma.LZMADecompressor().decompress(b'\x00' * 5)
except ValueError:
    pass
else:
    print('Failed')

# Test LZMADecompressor.decompress()
try:
    lzma.LZMADecompressor().decompress(b'\x00' * 13)
except ValueError:
    pass
else:
    print('Failed')

# Test LZMADecompressor.decompress()
try:
    lz
