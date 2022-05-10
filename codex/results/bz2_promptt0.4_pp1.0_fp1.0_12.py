import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

# Read a file in small chunks, decompress each chunk, and write the decompressed
# data to another file.
with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(decompressor.decompress(block))

# The decompressor object can also be used as a context manager.
# This is useful when working with file objects.

with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        decompressor = bz2.BZ2Decompressor()
        for block in iter(lambda: input.read(1024), b''):
            output.write(decompressor.decompress(block))

# Decompressor objects also have a flush() method that can be used to flush
# any remaining data
