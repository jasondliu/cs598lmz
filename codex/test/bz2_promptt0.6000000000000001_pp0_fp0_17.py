import bz2
# Test BZ2Decompressor on a single chunk of data

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
c = bz2.BZ2Decompressor()
decompressed_data = c.decompress(data)
print(decompressed_data)

# Test BZ2Decompressor on multiple chunks of data

decompressor = bz2.BZ2Decompressor()
with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem_decompressed.txt', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))
