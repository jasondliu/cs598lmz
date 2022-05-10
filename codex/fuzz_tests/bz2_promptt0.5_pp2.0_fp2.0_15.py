import bz2
# Test BZ2Decompressor

bz_file = bz2.BZ2File('data/articles.txt.bz2')
bz_decomp = bz2.BZ2Decompressor()

# Decompress first 10 bytes
bz_decomp.decompress(bz_file.read(10))

# Decompress the next 10 bytes
bz_decomp.decompress(bz_file.read(10))

# Decompress the rest of the file
bz_decomp.decompress(bz_file.read())

# Finish decompression
bz_decomp.flush()

# Close the file
bz_file.close()
 
# Test BZ2File

bz_file = bz2.BZ2File('data/articles.txt.bz2')

# Read the first 10 bytes
bz_file.read(10)

# Read the next 10 bytes
bz_file.read(10)

# Read the rest of the file
bz_file.read()

# Close the file

