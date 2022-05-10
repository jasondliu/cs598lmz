import mmap
import re

# create a file object
# This is a file object
file = open("test.txt", "r+")

# create a file-like object
# This is a memory-mapped file object
mapped_file = mmap.mmap(file.fileno(), 0)

# read file contents
print(mapped_file.read())

# read the first line
print(mapped_file.readline())

# read the next line
print(mapped_file.readline())

# read the rest of the file
print(mapped_file.readlines())

# search for a pattern
print(re.search(b"\d+", mapped_file))

# close the file-like object
mapped_file.close()

# close the file
file.close()
