import bz2
# Test BZ2Decompressor object
#
# Decompress and check against known good data
data = bz2.BZ2Compressor().compress(b"a" * 10)
data += bz2.BZ2Compressor().flush()

for i in range(3):
    d = bz2.BZ2Decompressor()
    result = d.decompress(data)
    print(result)
# Test BZ2Decompressor.seek()
#
# Decompress some known data, then seek back to beginning and decompress to a
# different end point.  We should get the same answer both times.

data = bz2.BZ2Compressor().compress(b"a" * 10)
data += bz2.BZ2Compressor().flush()

for i in range(3):
    d = bz2.BZ2Decompressor()
    result1 = d.decompress(data, 10)
