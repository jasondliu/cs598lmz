import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
        pass
# Test BZ2File

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    for block in iter(lambda: f.read(100), b''):
        pass
# Test BZ2File with decompress

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    for block in iter(lambda: f.read(100).decompress(), b''):
        pass
# Test BZ2File with decompress

with bz2.BZ2File('data/sample.bz2', 'rb') as f:
    for block in iter(lambda: f.read(100).decompress(), b''):
        pass
# Test
