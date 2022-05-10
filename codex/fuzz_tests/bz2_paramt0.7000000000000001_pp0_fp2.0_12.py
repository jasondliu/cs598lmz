from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

##Saving compressed data

import bz2
compressed_data = bz2.compress(original_data)
with open('uncompressed_data.bz2', 'wb') as f:
    f.write(compressed_data)
    
##Compressing data with zlib

import zlib
original_data = b'This is the original text.'
compressed_data = zlib.compress(original_data, level=9)
len(compressed_data)
decompressed_data = zlib.decompress(compressed_data)
decompressed_data


##Using lzma for compression
import lzma
compressed_data = lzma.compress(original_data)
decompressed_data = lzma.decompress(compressed_data)
decompressed_data
len(compressed_data)
len(decompressed_data)

##Dealing with tar files

import tarfile
with tarfile.open('some.tar.bz2', 'w
