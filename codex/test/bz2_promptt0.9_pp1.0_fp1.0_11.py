import bz2
# Test BZ2Decompressor.eof
b = bz2.BZ2Decompressor()
print(b.eof)			# 1
