import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/enwik8.bz2', 'rb') as input:
    with open('data/enwik8.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))
            if decompressor.unused_data:
                output.write(decompressor.unused_data)
                decompressor = bz2.BZ2Decompressor()
 
# Test BZ2File

with bz2.BZ2File('data/enwik8.bz2', 'rb') as input, open('data/enwik8.txt', 'wb') as output:
    for block in iter(lambda: input.read(100 * 1024), b''):
        output.write(block)
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/enwik8.txt', 'rb
