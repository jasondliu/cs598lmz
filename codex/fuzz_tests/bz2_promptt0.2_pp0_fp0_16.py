import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2_decompressor = bz2.BZ2Decompressor()

try:
    print(bz2_decompressor.decompress(data))
except OSError as err:
    print('OSError:', err)

print(bz2_decompressor.decompress(data[:-1]))
print(bz2_decompressor.decompress(data[:-4]))

try:
    print(bz2_decompressor.decompress(b'z'))
except OSError as err:
    print('OSError:', err)

try:
    print(bz2_decompressor.decompress(b'Z
