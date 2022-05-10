import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.open('example.bz2', 'rb') as input:
    with open('example.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# The above code is equivalent to:

with bz2.open('example.bz2', 'rb') as input:
    with open('example.out', 'wb') as output:
        output.write(decompressor.decompress(input.read()))

# The above code is also equivalent to:

with bz2.open('example.bz2', 'rb') as input:
    data = input.read()

with open('example.out', 'wb') as output:
    output.write(decompressor.decompress(data))
 
# To decompress data incrementally, use multiple calls to decompress():

with bz2.open('example.bz
