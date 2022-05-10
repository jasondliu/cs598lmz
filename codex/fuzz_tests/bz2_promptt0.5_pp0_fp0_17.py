import bz2
# Test BZ2Decompressor
decomp = bz2.BZ2Decompressor()
with open('data/test_file.txt.bz2', 'rb') as f:
    decomp.decompress(f.read())

# Test BZ2File
with bz2.BZ2File('data/test_file.txt.bz2', 'rb') as f:
    f.read()

# Test BZ2Compressor
comp = bz2.BZ2Compressor()
with open('data/test_file.txt', 'rb') as f:
    comp.compress(f.read())

# Test BZ2File
with bz2.BZ2File('data/test_file.txt.bz2', 'wb') as f:
    f.write(comp.flush())

# Test BZ2File
with bz2.BZ2File('data/test_file.txt.bz2', 'rb') as f:
    f.read()
