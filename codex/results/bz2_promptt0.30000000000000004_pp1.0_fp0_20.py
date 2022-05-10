import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/bz2_compressed_file.bz2', 'rb') as input:
    with open('data/bz2_uncompressed_file.txt', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(decompressor.decompress(block))

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/bz2_uncompressed_file.txt', 'rb') as input:
    with open('data/bz2_compressed_file_2.bz2', 'wb') as output:
        for block in iter(lambda: input.read(100 * 1024), b''):
            output.write(compressor.compress(block))
        output.write(compressor.flush())
 
 
# Test BZ2File

with bz2.BZ2File('data/bz2_comp
