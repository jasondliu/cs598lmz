import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?'
with bz2.BZ2Decompressor() as decompressor:
    print(decompressor.decompress(data))

print(decompressor.unused_data)

# Test BZ2Compressor
unused_data = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
compressor = bz2.BZ2Compressor()
print(compressor.compress(unused_data))
print(compressor.flush())

# Test BZ2File
with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
