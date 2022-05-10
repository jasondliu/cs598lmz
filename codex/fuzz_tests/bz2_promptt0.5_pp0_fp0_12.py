import bz2
# Test BZ2Decompressor
infile = bz2.BZ2File('compressed.bz2', 'rb')
outfile = open('uncompressed.txt', 'wb')
decompressor = bz2.BZ2Decompressor()

for block in iter(lambda: infile.read(100 * 1024), b''):
    outfile.write(decompressor.decompress(block))

outfile.close()
infile.close()
# Test BZ2Compressor
infile = open('uncompressed.txt', 'rb')
outfile = bz2.BZ2File('compressed.bz2', 'wb', compresslevel=9)
compressor = bz2.BZ2Compressor()

for block in iter(lambda: infile.read(100 * 1024), b''):
    outfile.write(compressor.compress(block))

outfile.write(compressor.flush())
outfile.close()
infile.close()
# Test BZ2File
infile = bz2.BZ2File('compressed.bz2
