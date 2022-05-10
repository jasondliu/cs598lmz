import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/sample.bz2') as src:
    unzipper = bz2.BZ2Decompressor()
    for block in iter(lambda: src.read(10 * unzipper.decompress_size), b''):
        data = unzipper.decompress(block)
        print(data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with open('data/sample.txt', 'rb') as src, open('data/sample.bz2', 'wb') as dst:
    for block in iter(lambda: src.read(64), b''):
        dst.write(compressor.compress(block))
    dst.write(compressor.flush())
 
# Compression and decompression with context managers

with bz2.open('data/sample.bz2', 'rb') as src, open('data/sample.txt', 'wb') as dst:
    dst.write(src.read())
 
with open('data/sample.
