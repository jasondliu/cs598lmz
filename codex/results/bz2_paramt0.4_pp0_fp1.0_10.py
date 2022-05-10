from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# Python 3.x
import bz2
bz2.decompress(bz2_data)

# Python 2.x
import bz2
bz2.decompress(bz2_data)

# Python 3.x
import gzip
with gzip.open('example.txt.gz', 'rt') as input_file:
    print(input_file.read())

# Python 2.x
import gzip
input_file = gzip.open('example.txt.gz', 'rb')
try:
    print(input_file.read())
finally:
    input_file.close()

# Python 3.x
import zlib
with open('lorem.txt', 'rb') as input:
    print(zlib.decompress(input.read(), 16+zlib.MAX_WBITS))

# Python 2.x
import zlib
input_file = open('lorem.txt', 'rb')
try:
    print(zlib.decompress(input_
