import bz2
# Test BZ2Decompressor with a file

# Test BZ2Decompressor with a file

import bz2

decompressor = bz2.BZ2Decompressor()

with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem_copy.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(decompressor.decompress(block))
# Test BZ2Decompressor with a file

import bz2

decompressor = bz2.BZ2Decompressor()

with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem_copy.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(decompressor.decompress(block))

print(decompressor.unused_data)
# Test BZ2Decompressor with a file

