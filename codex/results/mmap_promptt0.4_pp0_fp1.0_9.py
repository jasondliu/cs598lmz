import mmap
# Test mmap.mmap()

from mmap import *
import os

# create an empty file to work with
with open("testfile", "wb") as f:
    f.write(b"")

# open it for reading and writing
f = open("testfile", "r+b")

# create a memory mapped file
m = mmap(f.fileno(), 1024)

# write to the memory mapped file
m.write(b"Hello world")

# read from the memory mapped file
print(m.read(11))

# close the file
f.close()

# delete the file
os.unlink("testfile")

# Test mmap.mmap()

from mmap import *
import os

# create an empty file to work with
with open("testfile", "wb") as f:
    f.write(b"")

# open it for reading and writing
f = open("testfile", "r+b")

# create a memory mapped file
m = mmap(f.fileno(), 1024)

# write to the memory mapped file
m
