from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(s)

# For example, to decompress the first compressed string in the list, use:

BZ2Decompressor().decompress(data[0])

# In this exercise, you will use iterators to process the input data iteratively.

# Instructions

# Create a BZ2Decompressor object.
# Decompress the first 3 compressed lines in data. Assign the result to data_iter.
# Print the first 3 decompressed lines in data_iter.
# Hit 'Submit Answer' to print the sum of the lengths of the strings in data_iter.

# Create a BZ2Decompressor object
decompressor = BZ2Decompressor()

# Decompress the first 3 compressed lines
data_iter = (decompressor.decompress(line) for line in data[:3])

# Print the first 3 decompressed lines
print(next(data_iter))
print(next(data_iter))
print(next(data_iter))

# Sum the lengths of the strings in data_iter
print(sum(len(s)
