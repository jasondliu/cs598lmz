import bz2
# Test BZ2Decompressor
print('TEST BZ2Decompressor')
decompressor = bz2.BZ2Decompressor()

data = decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
print(data)

# Test BZ2File
print('TEST BZ2File')
with bz2.BZ2File('lorem.txt.bz2') as f:
    file_content = f.read()
    print(file_content)

# Test compress
print('TEST COMPRESS')
uncompressed_data = b'The same line, over and over.\n'
compressed_data = bz2.compress(uncompressed_data)
print(compressed_data)

# Test decompress
