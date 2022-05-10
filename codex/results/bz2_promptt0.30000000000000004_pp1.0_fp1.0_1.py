import bz2
# Test BZ2Decompressor
# with open('data/test.bz2', 'rb') as f:
#     decompressor = bz2.BZ2Decompressor()
#     with open('data/test.txt', 'wb') as g:
#         for data in iter(lambda: f.read(100 * 1024), b''):
#             g.write(decompressor.decompress(data))
#     g.write(decompressor.flush())

# Test BZ2Compressor
with open('data/test.txt', 'rb') as f:
    compressor = bz2.BZ2Compressor()
    with open('data/test.bz2', 'wb') as g:
        for data in iter(lambda: f.read(100 * 1024), b''):
            g.write(compressor.compress(data))
        g.write(compressor.flush())
