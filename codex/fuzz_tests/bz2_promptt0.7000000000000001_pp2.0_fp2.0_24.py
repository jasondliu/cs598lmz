import bz2
# Test BZ2Decompressor.
bz2_decomp = bz2.BZ2Decompressor()
print(bz2_decomp.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))
print(bz2_decomp.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))
# Test BZ2Compressor.
bz2_comp = bz2.BZ2Compressor()
print(bz2_comp.compress(b'Hello World'))
print(bz2_comp.flush())
