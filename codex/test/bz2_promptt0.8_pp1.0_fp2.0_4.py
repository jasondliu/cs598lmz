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
