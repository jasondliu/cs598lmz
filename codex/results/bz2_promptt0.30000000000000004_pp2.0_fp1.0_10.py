import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

decompressor = bz2.BZ2Decompressor()

for c in data:
    rv = decompressor.decompress(c)
    if rv:
        print(rv)

print(decompressor.flush())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

for i in range(300000):
    data = compressor.compress(b'foo')
    if data:
        print(data)

data = compressor.flush()
print(data)

# Test BZ2File

data = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00
