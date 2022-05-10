import bz2
# Test BZ2Decompressor

data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

decompressor = bz2.BZ2Decompressor()

decompressor.decompress(data)

decompressor.flush()

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

compressor.compress(b'foo')

compressor.compress(b'bar')

compressor.flush()

# Test BZ2File

with bz2.BZ2File('example.bz2', 'w') as output:
    output.write(b'Contents of the example file go here.\n')

with bz2.BZ2File('example.bz2', 'r') as input:
    print(
