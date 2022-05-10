import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input is {} bytes'.format(len(data)))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('Result is {} bytes'.format(len(result)))
print(result)

# Test BZ2File
uncompressed_data = open('lorem.txt', 'rb').read()
compressed_data = bz2.compress(uncompressed_data)
print('Compressed is {} bytes'.format(len(compressed_data)))

with bz2.open('lorem.bz2', 'wb') as output:
    output.write(compressed_data)

