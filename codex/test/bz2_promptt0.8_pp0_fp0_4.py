import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

text_file = open('bz2example.txt', 'wb')
in_file = open('example.bz2', 'rb')

try:
    print('start')
    while True:
        block = in_file.read(1024)
        if not block:
            break
        uncompressed = bz2_decompressor.decompress(block)
        if uncompressed:
            text_file.write(uncompressed)
    print('done')
finally:
    text_file.close()
    in_file.close()

# Test BZ2Compressor

import bz2

# Create the BZ2 compressor object
bz_comp = bz2.BZ2Compressor()

# Write the compressed data to a file
