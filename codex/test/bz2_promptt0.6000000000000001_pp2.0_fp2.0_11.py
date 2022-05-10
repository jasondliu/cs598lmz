import bz2
# Test BZ2Decompressor.__init__()

# Test BZ2Decompressor.__init__() with an argument
try:
    bz2.BZ2Decompressor(42)
except TypeError:
    pass
else:
    print('TypeError expected')

# Test BZ2Decompressor.__init__() with a non-integer argument
try:
    bz2.BZ2Decompressor('foo')
except TypeError:
    pass
else:
    print('TypeError expected')

# Test BZ2Decompressor.__init__() with a negative argument
