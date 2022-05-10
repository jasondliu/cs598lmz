import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
infile = open('../data/ch10/bz2_example.bz2', 'rb')
data = infile.read(100)
infile.close()
decompressor.decompress(data)
decompressor.unused_data

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
data = b'Lots of data here.\n'
compressor.compress(data)
compressor.flush()

# Test BZ2File
infile = bz2.BZ2File('../data/ch10/bz2_example.bz2', 'rb')
for line in infile:
    print(line)
infile.close()

infile = bz2.BZ2File('../data/ch10/bz2_example.bz2', 'rb')
data = infile.read()
infile.close()

outfile = bz2.BZ2File('../data/ch10/bz
