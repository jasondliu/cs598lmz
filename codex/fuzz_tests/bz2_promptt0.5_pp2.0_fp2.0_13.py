import bz2
# Test BZ2Decompressor.

import bz2

print 'Testing decompressor'

decompressor = bz2.BZ2Decompressor()

data = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

for c in data:
    r = decompressor.decompress(c)
    if r:
        print 'Decompressed:', repr(r)

print 'Decompressed:', repr(decompressor.decompress())
print 'Decompressed:', repr(decompressor.decompress())
print 'Done.'
