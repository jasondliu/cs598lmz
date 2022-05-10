import bz2
# Test BZ2Decompressor.multi_decompressor()
data = bz2.compress(b'\0' * 12000)

bzd = bz2.BZ2Decompressor()

