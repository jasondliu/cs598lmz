import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

d = bz2.BZ2Decompressor()
result = d.decompress(data)
result

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

compressor.compress(b'This is the first line.\n')

compressor.compress(b'And this is the second line.\n')

compressor.flush()

# Test BZ2File

with bz2.BZ2File('example.bz2', 'w') as output:
    for line in open('example.txt', 'rt'):
        output.write(line.encode('utf-8'))

with bz2.BZ2
