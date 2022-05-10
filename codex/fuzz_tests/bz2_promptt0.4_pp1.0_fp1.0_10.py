import bz2
# Test BZ2Decompressor

with bz2.open("../data/sample.bz2", "rb") as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress_block.__defaults__[0]), b''):
        print(decompressor.decompress(block))

# Test BZ2File

with bz2.open("../data/sample.bz2", "rb") as f:
    print(f.read())

# Test BZ2Compressor

with bz2.open("../data/sample.bz2", "rb") as f:
    compressor = bz2.BZ2Compressor()
    for block in iter(lambda: f.read(100 * compressor.compress_block.__defaults__[0]), b''):
        print(compressor.compress(block))
    print(compressor.flush())

# Test BZ2File

with bz2.open("../data/sample.bz2", "wb
