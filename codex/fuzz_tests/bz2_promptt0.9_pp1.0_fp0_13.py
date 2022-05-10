import bz2
# Test BZ2Decompressor
data = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
print(bz2.decompress(data))
print(bz2.decompress(data[0:4]))
print(bz2.decompress(data[4:9]))
print(bz2.decompress(data[4:13]))
print(bz2.decompress(data[4:47]))
# Test BZ2Compressor
data = "Lots of data".encode()
c = bz2.compress(data)
assert bz2.decompress(c) == data
# Test BZ2File
with BZ2File('/tmp/a-file.bz2', 'w') as file:
    file.write(data)
with B
