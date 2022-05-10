import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.decompress(data))
print(bz2.decompress(data[0:4]))
# Test BZ2Decompressor.decompress
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.decompress(data[0:4]))
# Test BZ2Decompressor.flush
print(decompressor.flush())
# Test BZ2Decompressor.decompress with multiple calls
decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data[:4]))
print(decompressor.decompress(data
