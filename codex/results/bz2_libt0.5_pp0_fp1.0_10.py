import bz2
bz2.decompress(compressed_data)

# The compression ratio is about 1.5 to 1.

# The bz2 module also provides a way to compress a file in one step and decompress it in another.

# Compress the contents of a file
in_file = open('lorem.txt', 'rb')
out_file = bz2.BZ2File('lorem.txt.bz2', 'wb')
out_file.writelines(in_file)
out_file.close()
in_file.close()

# Decompress the contents of the file
in_file = bz2.BZ2File('lorem.txt.bz2', 'rb')
out_file = open('lorem_copy.txt', 'wb')
out_file.writelines(in_file)
out_file.close()
in_file.close()

# The bz2 module also supports incremental compression and decompression.

# Create a compressor object
compressor = bz2.BZ2Compressor()

# Compress some data
for data in
