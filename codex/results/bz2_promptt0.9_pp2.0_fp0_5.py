import bz2
# Test BZ2Decompressor.unused_data behavior ...
obj = bz2.BZ2Decompressor()
obj.decompress(b'hello')
obj.unused_data

obj.decompress(b'world')
obj.unused_data

obj.flush()
obj.unused_data

obj.unused_data = b'xxx'
obj.unused_data

try:
    del obj.unused_data
except AttributeError:
    pass
else:
    print('unused_data property not write-once!')

# Test BZ2Decompressor.flush() behavior ...
testdata = b'x' * (10000 * 1000)
testdata = bz2.compress(testdata)
testdata = testdata + b'xxx'
obj = bz2.BZ2Decompressor()
obj.decompress(testdata)
obj.flush()
obj.flush()

# Test BZ2Decompressor.__getstate__(), .__setstate__() behavior ...
#   Ensure the state is picklable with and without
