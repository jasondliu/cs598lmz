import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
with open('data/data.bz2', 'rb') as f_compressed:
    with open('data/data.txt', 'wb') as f_decompressed:
        for chunk in iter(lambda: f_compressed.read(100 * 1024), b''):
            f_decompressed.write(decompressor.decompress(chunk))

# Test BZ2File

with bz2.BZ2File('data/data.bz2', 'rb') as f_compressed:
    with open('data/data.txt', 'wb') as f_decompressed:
        for chunk in iter(lambda: f_compressed.read(100 * 1024), b''):
            f_decompressed.write(chunk)
