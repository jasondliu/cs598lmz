import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))
decompressor = bz2.BZ2Decompressor()

print(decompressor)

result = decompressor.decompress(data)
print('Output is {} bytes'.format(len(result)))
print(result)

print(decompressor.decompress(data[0:4]))  # b'BZh'
print(decompressor.decompress(data[4:9]))  # b'91AY'
print(decompressor.decompress(data[9:14])) # b'&SY'

print(decompressor.decompress(data[10:14])) # b'SY'


