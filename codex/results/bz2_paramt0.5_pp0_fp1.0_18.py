from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# Example 2
from bz2 import open as bzopen
f = bzopen('file.bz2', 'rt')
for line in f:
    print(line)

# Example 3
import bz2
compressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
decompressor = bz2.BZ2Decompressor()
data = decompressor.decompress(compressed_data)
print(data)
