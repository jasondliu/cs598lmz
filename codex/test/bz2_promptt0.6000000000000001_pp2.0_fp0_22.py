import bz2
# Test BZ2Decompressor objects

import bz2

# Test decompressor objects

bzc = bz2.BZ2Compressor()
bzd = bz2.BZ2Decompressor()

data = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

d = bzc.compress(data)
d += bzc.flush()

bzd.decompress(d)
