import bz2
# Test BZ2Decompressor
with bz2.BZ2Decompressor() as decompressor:
    with gzip.open('../data/t10k-images-idx3-ubyte.gz', 'rb') as input:
        with open('../data/t10k-images-idx3-ubyte.bz2', 'wb') as output:
            for data in iter(lambda : input.read(100 * 1024), b''):
                output.write(decompressor.decompress(data))
# Test BZ2Compressor
with bz2.BZ2Compressor(9) as compressor:
    with open('../data/t10k-images-idx3-ubyte.bz2', 'rb') as input:
        with gzip.open('../data/t10k-images-idx3-ubyte.gz', 'wb') as output:
            for data in iter(lambda : input.read(100 * 1024), b''):
                output.write(compressor.compress(data))
            output.write(compressor.flush())
 

