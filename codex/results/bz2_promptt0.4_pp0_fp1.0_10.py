import bz2
# Test BZ2Decompressor
print(bz2.BZ2Decompressor().decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"))
# Test BZ2Compressor
print(bz2.BZ2Compressor().compress(b"hello"))

# Compress data
data = b"Lots of data here"
compressor = bz2.BZ2Compressor()
print(compressor.compress(data))
print(compressor.flush())

# Decompress data
compressed = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08
