import bz2
bz2c = bz2.BZ2Compressor()
print(bz2c.compress(b'hello world'))
print(bz2c.flush())

print(bz2.compress(b'hello world'))

bz2d = bz2.BZ2Decompressor()
print(bz2d.decompress(b'BZh91AY&SY\xd3\xee\x89\r\x00\x00\x00\x05\x00\x00\x00\x00\x80\x02\xff'))

data = open('lorem.txt', 'rb').read()
print(len(data))

compressed = bz2.compress(data)
print(len(compressed))

decompressed = bz2.decompress(compressed)
print(len(decompressed))
print(data == decompressed)

print(bz2.decompress(bz2.compress(data)))

import zlib
print(len(zlib.compress
