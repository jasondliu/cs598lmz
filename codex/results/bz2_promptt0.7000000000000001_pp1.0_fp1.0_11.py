import bz2
# Test BZ2Decompressor

with bz2.BZ2File('data/data.bz2') as bz2_file:
    bz2_file_contents = bz2_file.read()
    print(bz2_file_contents.decode())

# Decompressing with BZ2Decompressor
with bz2.BZ2File('data/data.bz2') as bz2_file:
    bz2_decompressor = bz2.BZ2Decompressor()
    bz2_file_contents = bz2_decompressor.decompress(bz2_file.read())
    print(bz2_file_contents.decode())

# Decompressing with BZ2File.read()
with bz2.BZ2File('data/data.bz2', 'rb') as bz2_file:
    bz2_file_contents = bz2_file.read()
    print(bz2_file_contents.decode())

# Decompressing with BZ
