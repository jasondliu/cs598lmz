import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample.bz2', 'rb') as input:
    with open('data/sample.out', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
            
        output.write(decompressor.flush())
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample.bz2', 'wb') as output:
    with open('data/sample.txt', 'rb') as input:
        while True:
            block = input.read(100 * 1024)
            if not block:
                break
            output.write(compressor.compress(block))
            
        output.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as input:
    with open
