import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Test BZ2Compressor
c = bz2.BZ2Compressor()
c.compress(b'hello world')
c.flush()

# Test compress and decompress
bz2.compress(b'hello world')
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# Test compress and decompress with compresslevel
bz2.
