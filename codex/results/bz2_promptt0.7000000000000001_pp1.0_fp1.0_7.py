import bz2
# Test BZ2Decompressor.
# From https://docs.python.org/3/library/bz2.html
# with open('lorem.txt', 'rb') as input:
#     with bz2.open('lorem.bz2', 'wb') as output:
#         output.writelines(input)

with open('lorem.bz2', 'rb') as input:
    with open('lorem_out.txt', 'wb') as output:
        decompressor = bz2.BZ2Decompressor()
        for block in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
        output.write(decompressor.flush())



# Let's test the same thing with lzma:
# https://docs.python.org/3/library/lzma.html
import lzma
with open('lorem.txt', 'rb') as input:
    with lzma.open('lorem.lzma', 'wb') as output:
        output.writelines(input)

