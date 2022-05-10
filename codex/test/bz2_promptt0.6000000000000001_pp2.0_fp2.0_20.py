import bz2
# Test BZ2Decompressor.__init__

d = bz2.BZ2Decompressor()
try:
    d.__init__()
except ValueError:
    pass
else:
    print("Unexpected success")

# Test BZ2Decompressor.decompress with non-string argument

d = bz2.BZ2Decompressor()
try:
    d.decompress(42)
except TypeError:
    pass
else:
    print("Unexpected success")

# Test BZ2Decompressor.decompress with a short input

d = bz2.BZ2Decompressor()
