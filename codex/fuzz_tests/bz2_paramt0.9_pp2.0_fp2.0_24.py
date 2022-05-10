from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(mybytes)

len(mybytes) 

###################################################################################################

#/usr/bin/env python
#import sys
#import os
#from bz2 import BZ2Decompressor

DATA_SIZE = 76649
BZ2_CHUNK_SIZE = 100000

cstream = BZ2Decompressor()
bz2data = sys.stdin.read(BZ2_CHUNK_SIZE)

decompressed_data = cstream.decompress(bz2data, max_length=DATA_SIZE)

while len(decompressed_data) < DATA_SIZE:
  bz2data = sys.stdin.read(BZ2_CHUNK_SIZE)
  if not bz2data:
    break
  decompressed_data = decompressed_data + cstream.decompress(bz2data)

print decompressed_data
