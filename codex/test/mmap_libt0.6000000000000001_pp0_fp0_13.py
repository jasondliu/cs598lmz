import mmap
import sys
import time

#
# Our test data
#
test_data = "Hello World"

#
# Our test file
#
test_file = "testfile.txt"

#
# Create a new file and write the data to it
#
f = open(test_file, "w+")
f.write(test_data)
f.close()

#
# Open the file
#
f = open(test_file, "r+")

#
# Create a memory map for the file
#
m = mmap.mmap(f.fileno(), 0)

#
# Read the data from the mapped file
#
