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
try:
    bz2.BZ2File(mode='r').__init__
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test decompress.__init__
try:
    bz2.decompress(compress(b'asdf')).__init__
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test compress.__init__
try:
    bz2.compress(b'asdf').__init__
except AttributeError:
    pass
else:
    print('AttributeError expected')

# Test B
