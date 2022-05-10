import bz2
bz2.decompress(gzippedSource)
 
#compress to bz2
import bz2

original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)

compressed = bz2.compress(original_data)
print('Compressed   :', len(compressed), compressed)

decompressed = bz2.decompress(compressed)
print('Decompressed :', len(decompressed), decompressed)



'''
Comparison of Compression
'''

import zlib
import bz2

original_data = b'This is the original text.'

print('Original     :', len(original_data), original_data)

with open('Example_4-4.py', 'rb') as input:
    original_data = input.read()
    print('Original     :', len(original_data))

with open('zlib.bin', 'wb') as output:
    output.write(zlib.compress(original_data))

with open
