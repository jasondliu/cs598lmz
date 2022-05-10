import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Decompress the entire file

with open('example.bz2', 'rb') as input:
    with open('uncompressed.txt', 'wb') as output:
        decompressor = bz2.BZ2Decompressor()
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
        output.write(decompressor.flush())
# Compress data iteratively

import bz2

compressor = bz2.BZ2Compressor()
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.flush()

# Compress an entire file

import bz2

with open('lorem.txt', 'rb') as input:
    with bz2.BZ2File('lorem.bz2', 'wb', compresslevel=9) as output
