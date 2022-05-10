import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2_decompressor = bz2.BZ2Decompressor()

try:
    print(bz2_decompressor.decompress(data))
except OSError as err:
    print('OS error: {0}'.format(err))

print(bz2_decompressor.decompress(data[0:-1]))
print(bz2_decompressor.decompress(data[0:-2]))
print(bz2_decompressor.decompress(data[0:-3]))

print(bz2_decompressor.unused_data)

print(bz2_decompressor.decompress(b'\x00
