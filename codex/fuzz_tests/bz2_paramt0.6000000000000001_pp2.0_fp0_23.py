from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# Output format
# userID,movieID,rating,timestamp

# The data is in a compressed bz2 file
# We need to decompress it first, then parse it

# We could write our own parsing code, but we'll use the built-in Python csv module instead

# This module provides a class to read data from a csv file, and a function to write data to a csv file

# We'll use the function to write decompressed data to a temporary csv file
# Then we'll use the class to read the data from the temporary file

# Let's open the bz2 file
data_file = bz2.open("../data/ml-1m/ratings.dat.bz2")

# We're going to write the decompressed data to a temporary csv file
# Let's create a variable to store the path to that file
temp_file = "../data/ml-1m/ratings.csv"

# Let's open the temporary file in write mode
temp_file_handle = open(temp_file, mode="wb")
