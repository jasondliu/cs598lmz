import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.decompress(data))
print(bz2.decompress(data[0:4]))
print(bz2.decompress(data[4:9]))
print(bz2.decompress(data[0:9]))

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
print(compressor.compress(b'foo'))
print(compressor.compress(b'foo'))
print(compressor.flush())

# Test BZ2File
with bz2.BZ2File('file.bz2', 'w') as f:
    f.write(b'foo')

with bz
