import bz2
# Test BZ2Decompressor
with bz2.BZ2File('../data/taxi.csv.bz2', 'r') as f:
    print(f.readline())

with bz2.BZ2File('../data/taxi.csv.bz2', 'r') as f:
    decompressor = bz2.BZ2Decompressor()
    for line in iter(lambda: f.read(100 * decompressor.decompress(f.read(100))), b''):
        print(line)
        break

# Test BZ2Compressor
with open('../data/taxi.csv', 'rb') as f_in:
    with bz2.BZ2File('../data/taxi.csv.bz2', 'wb') as f_out:
        compressor = bz2.BZ2Compressor()
        for data in iter(lambda: f_in.read(100), b''):
            f_out.write(compressor.compress(data))
        f_out.write(compressor.flush())

with bz2.
