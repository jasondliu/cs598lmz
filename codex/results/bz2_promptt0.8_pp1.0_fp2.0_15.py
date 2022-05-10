import bz2
# Test BZ2Decompressor

data = bz2.compress(b'This is an example of the bz2 module being used')

dec = bz2.BZ2Decompressor()
data = dec.decompress(data)
data

print(data)
