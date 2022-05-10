import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

d = bz2.BZ2Decompressor()
print(d.decompress(data))
print(d.decompress(b"\x00"))
print(d.decompress(b"BZh91AY&SY\x94$|\x0e\x00\x00"))
print(d.flush())

d = bz2.BZ2Decompressor()
print(d.decompress(data))
print(d.unused_data)
print(d.decompress(b"BZh91AY&SY\x94$|\x0e\x00\x00"))
print(d.unused_data)

d = bz2.B
