from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Compress data
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
len(data)

compressed = bz2.compress(data)
len(compressed)

bz2.decompress(compressed)

# Compress a file
import bz2
uncompressed = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
len(uncompressed)

with open('uncompressed.txt', '
