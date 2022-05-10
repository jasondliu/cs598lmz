import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()
# Test BZ2File
with open('file.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    with open('file.out', 'wb') as g:
        for block in iter(lambda: f.read(100 * 1024), b''):
            g.write(decompressor.decompress(block))

with open('file.out', 'rb') as f:
    compressed_data = f.read()

with open('file.bz2', 'wb') as f:
    compressor = bz2.BZ2Compressor()
    with open('file.in', 'rb') as g:
        for block in iter(lambda: g.read(100 * 1024), b''):
            f.write(comp
