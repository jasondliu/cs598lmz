import bz2
# Test BZ2Decompressor.decompress README example.

# Number of characters is a multiple of 1024.
data = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

print('Python', data)
