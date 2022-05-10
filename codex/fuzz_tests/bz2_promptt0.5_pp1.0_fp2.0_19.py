import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
data = data * 1000

cdata = bz2.compress(data)

print(len(data))
print(len(cdata))

d = bz2.BZ2Decompressor()
print(d.decompress(cdata))
print(d.unused_data)

d = bz2.BZ2Decompressor()
print(d.decompress(cdata[5:]))
print(d.unused_data)

d = bz2.BZ2Decompressor()
print(d.decompress(cdata[5:] + b'\0'))
print(d.unused_data)

d = bz2.BZ2Dec
