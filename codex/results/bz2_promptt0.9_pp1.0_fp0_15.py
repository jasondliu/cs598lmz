import bz2
# Test BZ2Decompressor.decompress by feeding it a large number of zero bytes.
# This leaked a small (1-32k) amount of memory on [pure] Pythons >= 2.5.2.
print bz2.decompress('\0' * 0x10000000)
print 'OKCompressLong'
