import bz2
# Test BZ2Decompressor
bz2_decomp = bz2.BZ2Decompressor()
print(bz2_decomp.decompress(bz2_data))

# Test BZ2File
bz2_file = bz2.BZ2File('bz2_file.bz2', 'w')
bz2_file.write(data)
bz2_file.close()

bz2_file = bz2.BZ2File('bz2_file.bz2', 'r')
print(bz2_file.read())
bz2_file.close()
