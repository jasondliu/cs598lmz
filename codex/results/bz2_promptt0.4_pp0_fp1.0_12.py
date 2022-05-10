import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()
uncompressed_data = bz2_decompressor.decompress(compressed_data)
uncompressed_data

# Test BZ2File
with bz2.BZ2File('uncompressed.txt.bz2', 'wb') as f:
    f.write(compressed_data)

with bz2.BZ2File('uncompressed.txt.bz2', 'rb') as f:
    uncompressed_data = f.read()
uncompressed_data

# Test BZ2File with context manager
with open('uncompressed.txt', 'rb') as f_in, bz2.BZ2File('uncompressed.txt.bz2', 'wb') as f_out:
    f_out.write(f_in.read())

with bz2.BZ2File('uncompressed.txt.bz2', 'rb') as f:
    uncompressed_data = f.read()
uncompressed_data
