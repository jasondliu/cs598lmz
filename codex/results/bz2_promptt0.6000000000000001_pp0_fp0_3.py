import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.decompress(data))
print(bz2.decompress(data[0:4]))
print(bz2.decompress(data[4:8]))
print(bz2.decompress(data[8:12]))
print(bz2.decompress(data[12:16]))
print(bz2.decompress(data[16:20]))
print(bz2.decompress(data[20:24]))
print(bz2.decompress(data[24:28]))
print(bz2.decompress(data[28:32]))
print(bz2.decompress(data[32:
