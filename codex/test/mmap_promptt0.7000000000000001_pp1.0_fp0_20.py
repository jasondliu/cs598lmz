import mmap
# Test mmap.mmap.read()
# Test mmap.mmap.read_byte()
# Test mmap.mmap.readline()
# Test mmap.mmap.readlines()
# Test mmap.mmap.seek()
# Test mmap.mmap.seekable()
# Test mmap.mmap.size()
# Test mmap.mmap.tell()
# Test mmap.mmap.write()
# Test mmap.mmap.write_byte()
# Test mmap.mmap.writelines()
# Test mmap.mmap.close()

import os, sys

filename = os.tmpnam()

# open file and write a line to it
f = open(filename, "w+")
f.write("foo\n")
f.close()

# map the file
m = mmap.mmap(f.fileno(), os.path.getsize(filename))

# read the line
line = m.readline()
assert line == "foo\n"

# change the line
m.seek(0)
