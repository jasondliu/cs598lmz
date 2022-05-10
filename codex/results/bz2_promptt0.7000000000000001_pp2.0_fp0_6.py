import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data.bz2') as src, \
     gzip.open('data.gz', 'wt') as dst:
    decompressor = bz2.BZ2Decompressor()
    while True:
        block = src.read(1024)
        if not block:
            break
        dst.write(decompressor.decompress(block))
    dst.write(decompressor.flush())
 
# Test BZ2Compressor

with gzip.open('data.gz', 'rt') as src, \
     bz2.BZ2File('data.bz2', 'wb') as dst:
    compressor = bz2.BZ2Compressor()
    while True:
        block = src.read(1024)
        if not block:
            break
        dst.write(compressor.compress(block))
    dst.write(compressor.flush())
 
# Test LZMACompressor

with open('data.txt', 'rb') as src, \
     lzma.open('
