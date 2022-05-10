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
print m.read(len(test_data))

#
# Seek to the beginning of the file and write new data
#
m.seek(0)
m.write("Hello World 2")

#
# Seek to the beginning of the file and read again
#
m.seek(0)
print m.read(len(test_data)+1)

#
# Close both the file and the memory map

