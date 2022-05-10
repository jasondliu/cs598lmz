import mmap
# Test mmap.mmap()

# This example uses mmap to create a file-backed array of integers.
# In this way, the entire array is not read into memory at once.
# Instead, memory is allocated on an as-needed basis - when an item
# is created or accessed.

# Note: This example may not work on Windows, but the code does
# work on Linux.

# Note: It is not possible to use the mmap module for regular files
# that are not backed by the operating system's virtual memory manager.

import mmap
import array
import os

# write a simple example file
with open("hello.txt", "wb") as f:
    f.write("Hello Python!\n".encode("ASCII"))

# Open the file for reading.
f = open('hello.txt', 'rb')

# Create a mmap instance with the following params:
# fileno: The file descriptor of the file to be memory-mapped.
# length: The number of bytes to map.
# flags: Maps prot (page protection) and flags values.
# Use mmap.ACCESS_READ to
