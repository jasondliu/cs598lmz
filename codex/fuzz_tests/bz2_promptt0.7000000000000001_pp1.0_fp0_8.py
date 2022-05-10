import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print("Input:")
print(data)

decompressor = BZ2Decompressor()
print("\nOutput:")
print(decompressor.decompress(data))
print(decompressor.unused_data)

decompressor = BZ2Decompressor()
print(decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))

# Test BZ2File
with BZ2File('test.bz2
