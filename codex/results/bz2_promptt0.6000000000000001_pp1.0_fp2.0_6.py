import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.decompress(data))
print(bz2.decompress(data))

d = bz2.BZ2Decompressor()
print(d.decompress(data))
print(d.decompress(data))
print(d.decompress(b'\x00\x00\x00\x07\x80\x04\x00\x00\x00'))
d.decompress(b'\x00\x00\x00\x07\x80\x04\x00\x00\x00')
print(d.unused_data)

# Test BZ2Compressor
data = b'BZh91AY&SY\
