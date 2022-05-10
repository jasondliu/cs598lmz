import bz2
# Test BZ2Decompressor's unused_data method.

decompressor = bz2.BZ2Decompressor()
try:
    decompressor.unused_data
except AttributeError:
    pass
else:
    print("AttributeError expected")

decompressor.decompress("BZ")
try:
    decompressor.unused_data
except ValueError:
    pass
else:
    print("ValueError expected")

data = bz2.compress("foo")
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)
try:
    decompressor.unused_data
except ValueError:
    pass
else:
    print("ValueError expected")

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data + "bar")
if decompressor.unused_data != "bar":
    print("unused_data expected to be 'bar', got %r" % decompressor.unused_data)

# Test BZ2Decompressor's flush method.

