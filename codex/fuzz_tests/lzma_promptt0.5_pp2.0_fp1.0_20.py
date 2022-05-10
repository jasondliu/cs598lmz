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
try:
    lzma.LZMADecompressor().flush()
except EOFError:
    pass
else:
    print('EOFError expected')
# Test LZMADecompressor.copy()
try:
    lzma.LZMADecompressor().copy()
except EOFError:
    pass
else:
    print('EOFError expected')
# Test LZMADecompressor.__copy__()
try:
    lzma.LZMADecompressor().__copy__()
except EOFError:
    pass
else:

