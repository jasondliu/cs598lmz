import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with bz2.BZ2File('data/python-2.7.13-docs-text.tar.bz2', 'rb') as input:
    with open('data/python-2.7.13-docs-text.tar', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/python-2.7.13-docs-text.tar', 'rb') as input:
    with bz2.BZ2File('data/python-2.7.13-docs-text.tar.bz2', 'wb') as output:
        for data in iter(lambda : input.read(100 * 1024), b''):
            output.write(compressor.compress(data))
            
        output.write(compressor.flush())
 
