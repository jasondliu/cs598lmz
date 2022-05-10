import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# Test BZ2File
with bz2.BZ2File('example.bz2', 'wb') as output:
    output.write(b'Contents of the example file go here.\n')

with bz2.BZ2File('example.bz2', 'rb') as input:
    print(input.read())

# Test compress
bz2.compress(b'Contents of the example file go here.\n')

# Test decompress
bz2.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00
