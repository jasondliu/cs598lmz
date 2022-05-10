import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('Output is {} bytes'.format(len(result)))
print(result)

print('Decompress the entire input')
decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
result += decompressor.flush()
print('Output is {} bytes'.format(len(result)))
print(result)

print('Decompress the entire input')
result = bz2.decompress(data)
print('Output is {} bytes'.format(len(result)))
print(result)

