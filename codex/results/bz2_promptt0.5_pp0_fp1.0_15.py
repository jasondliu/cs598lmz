import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'))

# Test BZ2File

with open('lorem.txt', 'rb') as input:
    with bz2.BZ2File('lorem.txt.bz2', 'wb') as output:
        output.writelines(input)

with bz2.BZ2File('lorem.txt.bz2', 'rb') as input:
    print(input.readline())

# Compressing and Decompressing Data

uncompressed_data = b'The same line, over and over.\n'

compressed = bz2.compress(uncompressed_data)

