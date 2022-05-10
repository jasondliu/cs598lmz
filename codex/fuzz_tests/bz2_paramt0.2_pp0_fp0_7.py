from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# The bz2 module includes a function for decompressing a whole file
# in one step

with open('example.bz2', 'rb') as input:
    decompressor = BZ2Decompressor()
    for block in iter(lambda: input.read(100 * 1024), b''):
        decompressed = decompressor.decompress(block)
        if decompressed:
            process_data(decompressed)
    remaining = decompressor.flush()
    if remaining:
        process_data(remaining)

# The bz2 module also includes a command line tool for decompressing files
# bzcat example.bz2

# The zlib module provides a lower-level interface based on the deflate
# algorithm. It is a bit more complicated to use directly, but it can be
# used to add compression to a program that does something else.

import zlib

compressed = zlib.compress(original_data)
decompressed = zlib.decompress(compressed)

# The zlib module provides
