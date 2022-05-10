import bz2
# Test BZ2Decompressor

data = bz2.compress(b"this is a test")
print(data)

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print(result)

decompressor = bz2.BZ2Decompressor()
try:
    decompressor.decompress(data[:-1])
except IOError as err:
    print("I/O error: {0}".format(err))

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data[:-1])
try:
    decompressor.decompress(b"garbage")
except IOError as err:
    print("I/O error: {0}".format(err))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
