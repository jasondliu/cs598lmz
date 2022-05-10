import bz2
# Test BZ2Decompressor.
source = bz2.compress(b'hello world')
print(source)
print(list(source))

# source = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# data = bz2.decompress(source)
# print(data)

# data = bz2.decompress(source)
# print(data)

source = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
source = iter(source)
