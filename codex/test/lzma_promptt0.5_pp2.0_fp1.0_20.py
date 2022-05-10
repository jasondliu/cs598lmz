import lzma
# Test LZMADecompressor.__init__()
try:
    lzma.LZMADecompressor()
except TypeError:
    pass
else:
    print('TypeError expected')
# Test LZMADecompressor.decompress()
try:
    lzma.LZMADecompressor().decompress(b'')
except EOFError:
    pass
else:
    print('EOFError expected')
# Test LZMADecompressor.flush()
