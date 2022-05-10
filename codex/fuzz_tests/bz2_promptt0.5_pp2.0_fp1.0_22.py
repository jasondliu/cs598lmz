import bz2
# Test BZ2Decompressor
#data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
#print(bz2.BZ2Decompressor().decompress(data))
#print(bz2.decompress(data))

# Test BZ2Compressor
#compressor = bz2.BZ2Compressor()
#print(compressor.compress(b'hello'))
#print(compressor.compress(b'world'))
#print(compressor.flush())

# Test BZ2File
#with bz2.BZ2File('example.bz2', 'wb') as output:
#    with open('example.txt', 'rb') as input:
#        output.write(input.read())
#
#with bz2.BZ2File('
