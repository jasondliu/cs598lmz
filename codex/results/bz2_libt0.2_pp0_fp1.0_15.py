import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File
bz2_file = bz2.BZ2File('example.bz2')
bz2_file.read()
bz2_file.close()

# bz2.compress()
bz2.compress(data)

# bz2.open()
bz2.open('example.bz2', mode='wt')

# bz2.compressfile()
with open('example.bz2', 'rb') as input:
    bz2.compressfile(input)

# bz2.decompressfile()
with open('example.bz2', 'rb') as input:
    bz2.decompressfile(input)

# bz2.BZ2Compressor()
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# bz2.BZ2Decompressor()
decompressor = bz2.BZ
