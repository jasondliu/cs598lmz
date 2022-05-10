import bz2
# Test BZ2Decompressor
d = bz2.BZ2Decompressor()
decompressed_data = d.decompress(compressed_data)
decompressed_data

# Test compress
d.decompress(d.unused_data)

with bz2.BZ2File(('sample.bz2'), 'wb') as f:
    f.write(data)
    f.write(data)

with bz2.BZ2File(('sample.bz2'), 'rb') as f:
    print(f.read())
    f.seek(0)
    for line in f:
        print(line.strip())
