import bz2
# Test BZ2Decompressor

# Example 1
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print(bz2.decompress(data))

# Example 2
with bz2.BZ2File('example.bz2', 'rb') as input:
    with open('example.out', 'wb') as output:
        decompressor = bz2.BZ2Decompressor()
        for block in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
