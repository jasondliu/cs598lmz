import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
data = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
data = bz2_decompressor.decompress(data)
print(data)

# Test BZ2Compressor
bz2_compressor = bz2.BZ2Compressor()
data = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
data = bz2_compressor.compress(data)
print(data)

