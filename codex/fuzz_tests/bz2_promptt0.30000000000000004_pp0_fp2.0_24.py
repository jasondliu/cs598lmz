import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/compressed_file.bz2', 'rb') as input:
    with open('data/uncompressed_file.txt', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/uncompressed_file.txt', 'rb') as input:
    with open('data/compressed_file.bz2', 'wb') as output:
        for data in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(data))
        output.write(compressor.flush())
 
# Test BZ2File

with bz2.BZ2File('data/compressed_file.bz2', 'rb') as input:
    data = input.read()

