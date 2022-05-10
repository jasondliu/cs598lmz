import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes long'.format(len(data)))

decompressor = bz2.BZ2Decompressor()

for i in range(1, 10):
    result = decompressor.decompress(data)
    print('{} {} bytes: {!r}'.format(i, len(result), result))
    if not result:
        break
    print('Still contains {} bytes of compressed data'.format(len(decompressor.unused_data)))

print('Unused data after loop exited: {}'.format(decompressor.unused_data))

compressor = bz2.BZ2Compressor()
for i in range(1, 10):
    result = compressor.compress(
