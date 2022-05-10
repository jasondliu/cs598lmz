import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2_decompressor = bz2.BZ2Decompressor()

try:
    print(bz2_decompressor.decompress(data))
    print(bz2_decompressor.flush())

except EOFError:
    pass

# Test BZ2Compressor

data = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
bz2_compressor = bz2.BZ2Compressor(9)


