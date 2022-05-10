import bz2
# Test BZ2Decompressor
with bz2.BZ2File('./data/sample.bz2') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
        pass
# Test BZ2File
with bz2.BZ2File('./data/sample.bz2') as f:
    for line in f:
        pass
# Test BZ2File with decompression
with bz2.BZ2File('./data/sample.bz2', 'rb') as f:
    for line in f:
        pass
# Test BZ2File with compression
with bz2.BZ2File('./data/sample.bz2', 'wb') as f:
    f.write(b'Hello World!')
# Test BZ2File with compression and buffering
with bz2.BZ2File('./data/sample.bz2', 'wb', compresslevel=9) as f:

