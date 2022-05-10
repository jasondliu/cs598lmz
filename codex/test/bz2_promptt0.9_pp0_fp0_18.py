import bz2
# Test BZ2Decompressor with a stream with multiple members
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\xd0\x00\x00\x00#\x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
bz2_file = bz2.BZ2Decompressor()
uncompressed_data = bz2_file.decompress(data)
print(uncompressed_data)

uncompressed_data = bz2_file.decompress(bz2_file.unused_data)
print(uncompressed_data)

if bz2_file.eof:
    print('All data successfully decompressed')

print('Done')
 

import struct
# read and unpack a binary file
