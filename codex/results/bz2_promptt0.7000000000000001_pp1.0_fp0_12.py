import bz2
# Test BZ2Decompressor
with bz2.BZ2File('example.bz2') as input:
    with open('uncompressed.txt', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(data)
 
# Test BZ2Compressor
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
with open('uncompressed.txt', 'wb') as output:
    output.write(data)
with open('uncompressed.txt', 'rb') as input:
    with bz2.BZ2File('example.bz2', 'wb') as output:
        output.write(input.read())
 
# Test open
with bz2.open('example.bz2', mode='wt
