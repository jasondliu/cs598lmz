import lzma
# Test LZMADecompressor.__init__()

# This test fails with Python 2.7.2

try:
    lzma.LZMADecompressor(format=lzma.FORMAT_ALONE)
except lzma.LZMAError:
    pass
else:
    print('no error')
# Test LZMADecompressor.decompress()

# This test fails with Python 2.7.2

try:
    lzma.LZMADecompressor().decompress(b'\x00')
except lzma.LZMAError:
    pass
else:
    print('no error')
# Test LZMADecompressor.decompress()

# This test fails with Python 2.7.2

try:
    lzma.LZMADecompressor().decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00')
except lzma.LZMAError:
    pass
else:
    print('no error')
