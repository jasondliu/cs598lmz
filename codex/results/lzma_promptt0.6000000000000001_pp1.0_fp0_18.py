import lzma
# Test LZMADecompressor.__init__()
try:
    lzma.LZMADecompressor(dict_size=-1)
except ValueError:
    pass
else:
    print('Failed to raise ValueError when dict_size is negative')
# Test LZMADecompressor.decompress()
try:
    lzma.LZMADecompressor().decompress(b'x' * lzma.LZMA_CHECK_SIZE)
except ValueError:
    pass
else:
    print('Failed to raise ValueError when LZMA_CHECK_SIZE bytes are not available')
try:
    lzma.LZMADecompressor().decompress(b'x' * lzma.LZMA_CHECK_SIZE + b'\x00')
except ValueError:
    pass
else:
    print('Failed to raise ValueError when LZMA_CHECK_SIZE bytes are not available')
try:
    lzma.LZMADecompressor().decompress(b'\x00' * lzma.LZMA
