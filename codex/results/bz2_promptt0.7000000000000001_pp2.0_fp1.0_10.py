import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

print(decompressor.decompress(data[0:4]))
print(decompressor.decompress(data[4:10]))
print(decompressor.decompress(data[10:]))
print(decompressor.decompress(data[10:14]))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
print(compressor.compress(b'foo'))
print(compressor.flush())

# Compression ratio
original = b'This is the original text.'
comp
