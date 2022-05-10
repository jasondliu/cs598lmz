import bz2
# Test BZ2Decompressor object

print('creating decompressor')
decompressor = BZ2Decompressor()

print('feeding decompressor with compressed data')
data = decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
data += decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

print(data)

import bz2

# Open an existing file to compress using bz2 module
f1 = bz2.open('file1.txt','wb')
f1.write('BZh
