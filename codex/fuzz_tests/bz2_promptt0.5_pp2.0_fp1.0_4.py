import bz2
# Test BZ2Decompressor
#
# First, create a compressed file

with open('lorem.txt', 'rb') as input:
    with bz2.BZ2File('lorem.bz2', 'wb', compresslevel=9) as output:
        output.writelines(input)
# Now, read the compressed data

decompressor = bz2.BZ2Decompressor()

with open('lorem.bz2', 'rb') as input:
    with open('lorem.txt.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
# The compressed file is quite small

!ls -l lorem.bz2

# And the decompressed file matches the original

!diff lorem.txt lorem.txt.out

# Clean up

!rm lorem.txt.out lorem.bz2
 
# Test BZ2Compressor
#
# First, create a compressed file

with open('lorem.
