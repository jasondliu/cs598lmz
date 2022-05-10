import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
for chunk in iter(lambda: f.read(100 * 1024), b''):
    rv = decompressor.decompress(chunk)
    if rv:
        print(rv)

# Test BZ2File
with bz2.BZ2File('filename.bz2', 'rb') as f:
    print(f.read(100))

# Test compress()
data = b"Lots of data here."
compressed = bz2.compress(data)
# Test decompress()
decompressed = bz2.decompress(compressed)
