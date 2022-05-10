import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Hello World')
print(data)

decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(data))
except EOFError:
    print('Not enough data to decompress')

decompressor.decompress(data[:-1])
decompressor.decompress(data[-1:])

print(decompressor.flush())

print(decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))

print(decompressor.flush())

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

for i in range(5):
    print(compressor
