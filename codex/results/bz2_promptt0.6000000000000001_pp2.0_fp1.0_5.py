import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(len(data))

decompressor = bz2.BZ2Decompressor()

try:
    print(decompressor.decompress(data))
    print(decompressor.flush())

except IOError as e:
    print('Not compressed data')
    print(e)

decompressor = bz2.BZ2Decompressor()

for chunk in [data[:4], data[4:10], data[10:16], data[16:], b'\x00']:
    try:
        print(decompressor.decompress(chunk))
    except IOError:
        print('Not compressed data')

print(decompressor.flush())
