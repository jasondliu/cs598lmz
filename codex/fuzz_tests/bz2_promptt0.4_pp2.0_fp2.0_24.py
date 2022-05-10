import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is %d bytes' % len(data))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print('Output is %d bytes' % len(decompressor.decompress(data)))
print('Remaining %d bytes' % len(decompressor.unused_data))

decompressor = bz2.BZ2Decompressor()
for block in [data[0:4], data[4:8], data[8:12], data[12:16]]:
    print(decompressor.decompress(block))
print(decompressor.flush())

decompressor = bz2.BZ2Dec
