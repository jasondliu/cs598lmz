from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Compression
import bz2
for i in range(1, 10):
    s = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    print(i, len(s), len(bz2.compress(s, i)))

# Compression
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)
decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)

# Compression
import bz2
original_data
