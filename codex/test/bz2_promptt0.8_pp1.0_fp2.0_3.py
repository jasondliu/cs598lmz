import bz2
# Test BZ2Decompressor.__init__
try:
    bz2.BZ2Decompressor().__init__
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test BZ2Compressor.__init__
try:
    bz2.BZ2Compressor().__init__
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test BZ2File.__init__
