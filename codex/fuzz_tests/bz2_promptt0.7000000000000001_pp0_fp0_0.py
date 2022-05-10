import bz2
# Test BZ2Decompressor

# Input file
sourceFile = 'example.txt.bz2'

# Output file
targetFile = 'uncompressed.txt'

# Read in the compressed input file
with bz2.BZ2File(sourceFile, 'rb') as infile:
    decompressor = bz2.BZ2Decompressor()
    with open(targetFile, 'wb') as outfile:
        for data in iter(lambda: infile.read(100 * 1024), b''):
            outfile.write(decompressor.decompress(data))
# Test BZ2Compressor

# Input file
sourceFile = 'example.txt'

# Output file
targetFile = 'example.txt.bz2'

# Read in the input file
with open(sourceFile, 'rb') as infile:
    with bz2.BZ2File(targetFile, 'wb') as outfile:
        compressor = bz2.BZ2Compressor()
        for data in iter(lambda: infile.read(100 * 1024), b''):
            outfile
