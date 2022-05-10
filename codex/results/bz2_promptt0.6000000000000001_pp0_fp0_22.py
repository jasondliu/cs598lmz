import bz2
# Test BZ2Decompressor
bz2_decomp = bz2.BZ2Decompressor()

# Decompress and print first 5 bytes
data = bz2_decomp.decompress(bz2_data)

# Print the first 5 bytes of the decompressed data
print(data[:5])

# Decompress and print the rest of the data
data = bz2_decomp.decompress(data[5:])
print(data)

# Decompress and print the rest of the data
print(bz2_decomp.decompress(data))

# Decompress and print the rest of the data
print(bz2_decomp.decompress())

# End of the stream has been reached
print(bz2_decomp.eof)

# The decompressor object can be used as a context manager
with bz2.BZ2Decompressor() as bz2_decomp:
    print(bz2_decomp.decompress(bz2_data))
 
# Import pickle package
import pickle

