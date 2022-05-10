import bz2
# Test BZ2Decompressor() function
# It's a good idea to play with the bz2 module. Here is a way to decompress a file, one chunk at a time:

decompressor = bz2.BZ2Decompressor()

with open('file.bz2', 'rb') as input:
    with open('file.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            out = decompressor.decompress(block)
            if out:
                output.write(out)
# Test the compress() function
with open('file.txt', 'rb') as input:
    data = input.read()

compressed = bz2.compress(data)
# Test the open() function
# The open() function works with a filename. It also has useful optional arguments for controlling the buffering policy when reading and writing.

import bz2

un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0
