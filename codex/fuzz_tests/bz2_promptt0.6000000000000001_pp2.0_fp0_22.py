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
bzd.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

bzd.flush()
bzd.unused_data

bzd.decompress(d)
bzd.unused_data

bzd.flush()

# Test incremental decompression

b
