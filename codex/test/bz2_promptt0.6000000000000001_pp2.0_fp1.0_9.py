import bz2
# Test BZ2Decompressor's unused_data method.

decompressor = bz2.BZ2Decompressor()
try:
    decompressor.unused_data
except AttributeError:
    pass
else:
    print("AttributeError expected")

