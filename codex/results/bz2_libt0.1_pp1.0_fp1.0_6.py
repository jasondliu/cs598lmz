import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File
bz2_file = bz2.BZ2File('example.bz2')
bz2_file.read()
bz2_file.close()

# bz2.compress
bz2.compress(data)

# bz2.open
bz2.open('example.bz2', mode='wt')

# bz2.compressfile
bz2.compressfile(open('example.txt', 'rb'))

# bz2.decompressfile
bz2.decompressfile(bz2.compressfile(open('example.txt', 'rb')))
