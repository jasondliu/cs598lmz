import lzma
# Test LZMADecompressor.__init__()
try:
    lzma.LZMADecompressor()
except TypeError:
    pass
else:
    print('TypeError expected')

# Test LZMADecompressor.__init__(format=FORMAT_AUTO)
try:
    lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
except TypeError:
    pass
else:
    print('TypeError expected')

# Test LZMADecompressor.__init__(format=FORMAT_XZ)
try:
    lzma.LZMADecompressor(format=lzma.FORMAT_XZ)
except TypeError:
    pass
else:
    print('TypeError expected')

# Test LZMADecompressor.__init__(check=-1)
try:
    lzma.LZMADecompressor(check=-1)
except ValueError:
    pass
else:
    print('ValueError expected')

# Test LZMADecompressor
