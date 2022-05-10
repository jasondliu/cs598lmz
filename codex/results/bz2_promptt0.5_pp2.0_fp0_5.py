import bz2
# Test BZ2Decompressor
data = open('../data/sample.bz2', 'rb').read()

decompressor = bz2.BZ2Decompressor()

print(decompressor.decompress(data))

print(decompressor.decompress(data[:10]))

print(decompressor.decompress(data[10:]))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

print(compressor.compress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))

print(compressor.compress(b'hello'))

print(compressor.flush())


# Test BZ2File

with bz2.open('../data/sample.bz2', mode='rt') as
