import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('DATA:', len(data))

decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(data)
print('RESULT:', len(result))

print('SAME:', data == result)

# Test BZ2File

uncompressed_data = open('lorem.txt', 'rb').read()
print('ORIGINAL:', len(uncompressed_data))

compressed_file = bz2.BZ2File('lorem.txt.bz2', 'wb')
compressed_file.write(uncompressed_data)
compressed_file.close()

compressed_data = open('lorem.txt.b
