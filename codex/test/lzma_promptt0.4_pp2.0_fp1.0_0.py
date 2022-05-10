import lzma
# Test LZMADecompressor.__init__()
try:
    lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
except ValueError:
    pass
else:
    print('ValueError expected')

try:
    lzma.LZMADecompressor(memlimit=1)
except ValueError:
    pass
else:
    print('ValueError expected')

try:
    lzma.LZMADecompressor(memlimit=1 << 40)
except ValueError:
    pass
else:
    print('ValueError expected')

try:
    lzma.LZMADecompressor(filters=[{'id': lzma.FILTER_LZMA2}])
except ValueError:
    pass
else:
    print('ValueError expected')

try:
    lzma.LZMADecompressor(filters=[{'id': lzma.FILTER_LZMA2, 'dict_size': 1}])
except ValueError:
    pass
