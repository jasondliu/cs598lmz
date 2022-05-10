import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File
bz2_file = bz2.BZ2File('example.bz2')
bz2_file.read()

# bz2.compress
bz2.compress(data)

# bz2.decompress
bz2.decompress(bz2_data)
