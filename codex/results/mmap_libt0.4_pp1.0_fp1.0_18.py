import mmap
import sys

# Global variables

# The name of the file to read
filename = "data.txt"

# The number of bytes to read at a time
chunk_size = 1024

# The number of times to read the file
number_of_reads = 10

# Open the file
file = open(filename, "r")

# Create a file mapping
mapping = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)

# Print the file to the screen
for i in range(number_of_reads):
    print(mapping.read(chunk_size))

# Close the file
file.close()

# Print a blank line
print()

# Open the file
file = open(filename, "r")

# Use the file object to read the file
for i in range(number_of_reads):
    print(file.read(chunk_size))

# Close the file
file.close()

# Print a blank line
print()

# Open the file
file = open(filename
