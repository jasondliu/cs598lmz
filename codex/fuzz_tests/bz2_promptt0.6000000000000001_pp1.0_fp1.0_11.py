import bz2
# Test BZ2Decompressor

with bz2.open('<your-file>', 'rb') as input:
    with open('<your-output-file>', 'wb') as output:
        decompressor = BZ2Decompressor()
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
 
# Test BZ2Decompressor

with bz2.open('<your-file>') as input:
    with open('<your-output-file>', 'wb') as output:
        decompressor = BZ2Decompressor()
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
 
 
# Test BZ2Decompressor

with bz2.open('<your-file>') as input:
    with open('<your-output-file>', 'wb') as output:
        decompressor = BZ2Decompressor()
        for block in iter(lambda: input
