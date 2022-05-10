import bz2
bz2.BZ2File

# If you want to check that your code works on little-endian platforms,
# you can use the sys.byteorder check. sys.byteorder will be either 'little' or 'big'.
# (See https://docs.python.org/3/library/sys.html#sys.byteorder)
import sys
sys.byteorder

# This is a string.
x = 'Platypus'

# Convert a string to ASCII code and vice-versa.
ord('A')
chr(65)

# String slices are accessible with the syntax that works on lists.
# The only difference is that indices are treated as character positions.
x[4]

# You can also use negative indices, which count from the right.
x[-1]

# This is a list.
x = [1, 2, 3]

# Lists are ordered sets of objects, and can contain objects of different types.
x = [1, 'bear', 3.14]

# Use the append method to add to the end of a list.
x.append(1)

