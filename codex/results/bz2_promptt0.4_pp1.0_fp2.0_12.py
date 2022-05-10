import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('enwik9.bz2', 'rb') as f:
    for data in iter(lambda: f.read(100 * 1024), b''):
        print(bz2_decompressor.decompress(data))
        print(len(bz2_decompressor.unused_data))

# Test BZ2File

with bz2.BZ2File('enwik9.bz2') as f:
    for line in f:
        print(line)

# Test open

with bz2.open('enwik9.bz2', 'rt') as f:
    for line in f:
        print(line)

# Test compress

with open('enwik9.bz2', 'rb') as f_in, open('enwik9.bz2.out', 'wb') as f_out:
    f_out.write(bz2.compress(f_in.read()))

# Test decompress
