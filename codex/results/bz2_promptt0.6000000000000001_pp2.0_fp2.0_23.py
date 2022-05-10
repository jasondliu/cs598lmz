import bz2
# Test BZ2Decompressor
with open('data/test.bz2', 'rb') as f:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: f.read(100 * 100), b''):
        print(decompressor.decompress(block))

# Test BZ2Compressor
with open('data/test.bz2', 'rb') as f_input, \
        bz2.open('data/test_compressed.bz2', 'wb') as f_output:
    for line in f_input:
        f_output.write(line)

# Test BZ2File
with bz2.open('data/test.bz2', 'rb') as f:
    for line in f:
        print(line)
