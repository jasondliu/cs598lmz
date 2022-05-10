import bz2
# Test BZ2Decompressor and BZ2Compressor classes

d = bz2.BZ2Decompressor()
d.decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")
d.decompress(b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08")
print(d.flush())

c = bz2.BZ2Compressor()
c.compress(b"this is a test")
c.compress(b"this is another test")
c.flush()
c.compress(b"and some directly compressed string")
print(
