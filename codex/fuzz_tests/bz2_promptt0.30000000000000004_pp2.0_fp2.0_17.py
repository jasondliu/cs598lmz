import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
print('Output is {} bytes'.format(decompressor.decompress(data)))
print('Remaining {} bytes'.format(decompressor.unused_data))

decompressor = bz2.BZ2Decompressor()
for chunk in data:
    print(decompressor.decompress(chunk))
print('Remaining {} bytes'.format(decompressor.unused_data))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print('Remaining {} bytes'.format(decompressor.un
