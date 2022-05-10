import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
d.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
d.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')
d.flush()

# Test BZ2Decompressor.__init__
bz2.BZ2Decompressor()

# Test BZ2Decompressor.decompress
d.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\
