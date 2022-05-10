import bz2
bz2.decompress(bz2_data)

# bz2.BZ2File
bz2_file = bz2.BZ2File('file.bz2')
bz2_file.read()
bz2_file.close()

# bz2.compress
bz2.compress(data)

# bz2.open
bz2.open('file.bz2', mode='wt')
bz2.open('file.bz2', mode='wt', compresslevel=9)

# bz2.compresslevel
bz2.compresslevel

# bz2.decompress
bz2.decompress(bz2_data)

# bz2.BZ2File
bz2.BZ2File('file.bz2')
bz2.BZ2File('file.bz2', mode='wt')
bz2.BZ2File('file.bz2', mode='wt', compresslevel=9)

# bz2.BZ2File.
