import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# bz2.decompress(bz2.compress(b'hello world!'))

import zlib
zlib.compress(b'hello world!')
# zlib.compress(b'hello world!')

zlib.decompress(zlib.compress(b'hello world!'))

# zlib.decompress(zlib.compress(b'hello world!'))

# zlib.crc32(b'hello world!')

from struct import Struct

def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

records = [ (1, 2.3, 4.5),
            (6, 7.8, 9.0),
            (12, 13.4, 56.7) ]

with
