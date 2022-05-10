import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

data = decompressor.decompress(bz2_data)
data

# Test BZ2File

bz2_file = bz2.BZ2File('bz2_file.bz2')

data = bz2_file.read()
data

# Compress a file

bz2_file = bz2.BZ2File('bz2_file.bz2', 'w')

bz2_file.write(data)
bz2_file.close()

# Test BZ2File with context manager

with bz2.BZ2File('bz2_file.bz2', 'w') as bz2_file:
    bz2_file.write(data)

# Test BZ2File with context manager and read

with bz2.BZ2File('bz2_file.bz2', 'r') as bz2_file:
    data = bz2_file.read()

