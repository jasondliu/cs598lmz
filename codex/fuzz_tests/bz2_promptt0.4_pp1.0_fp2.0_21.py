import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('sample.bz2', 'rb') as input:
    with open('sample.xml', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2File

with bz2.BZ2File('sample.bz2', 'rb') as input, open('sample.xml', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(block)
 
# Test BZ2File with decompressor

with bz2.BZ2File('sample.bz2', 'rb') as input, open('sample.xml', 'wb') as output:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(decompressor.decompress(block
