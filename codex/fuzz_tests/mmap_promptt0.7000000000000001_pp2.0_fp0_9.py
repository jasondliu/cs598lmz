import mmap
# Test mmap.mmap(0,1)
#
# HISTORY
# 17-Dec-1999 (bonnie)
#	Created.
#
#***********************************************************************

import os
import signal
import sys

test_case = "t0014"

test_file = os.path.normpath(os.getcwd() + "/" + test_case + ".dat")

# File size is 1 byte.
test_size = 1

# Open a file to write to.
file = open(test_file, "w+")

# Write the test string to the file.
file.write("1\n")

# Close the file.
file.close()

# Open a file to read from.
file_to_read = open(test_file, "r+")

# Map the file into shared memory.
map = mmap.mmap(file_to_read.fileno(), test_size)

# Read from the map.
read_data = map.read(test_size)
print read_data

# Unmap the file.
map.close()

