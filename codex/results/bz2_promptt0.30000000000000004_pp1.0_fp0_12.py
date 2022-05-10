import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.unused_data)

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data[:-1]))
print(decompressor.unused_data)

decompressor = bz2.BZ2Decompressor()
try:
    decompressor.decompress(data[:-10])
except IOError as e:
    print(e)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
print(compressor.comp
