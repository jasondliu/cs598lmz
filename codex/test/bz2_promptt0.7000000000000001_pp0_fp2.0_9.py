import bz2
# Test BZ2Decompressor for read() method

print('creating BZ2Decompressor object')
d = bz2.BZ2Decompressor()

# The incompressible data is long enough that it will
# not be buffered by the compressor
data = d.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

