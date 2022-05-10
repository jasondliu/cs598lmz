import bz2
# Test BZ2Decompressor's ability to handle errors.
decomp = bz2.BZ2Decompressor()
b = decomp.decompress(b'BZh91AY&SY') # No errors raised
