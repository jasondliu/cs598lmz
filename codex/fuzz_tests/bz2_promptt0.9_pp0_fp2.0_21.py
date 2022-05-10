import bz2
# Test BZ2Decompressor
print(bz2.decompress("BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"))

# Test BZIP2 Compressers
data = "Hello World"
data = data.encode('utf-8')
# Using BZ2Compressor object
bz2comp = bz2.BZ2Compressor()
bz2data = bz2comp.compress(data)
bz2data = bz2data + bz2comp.flush()
print(bz2data.decode('utf-8'))

# Using BZ2Compresser compile method
comprule = 'compress'
bz2data = bz2.compress(data, comprule)
print(bz2data.decode('utf-8'))

# Using BZ2
