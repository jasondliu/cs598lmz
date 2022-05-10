import bz2
# Test BZ2Decompressor
with bz2.BZ2File('lorem.txt.bz2') as src, open('lorem_copy.txt', 'wb') as dst:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: src.read(1024), b''):
        dst.write(decompressor.decompress(block))

