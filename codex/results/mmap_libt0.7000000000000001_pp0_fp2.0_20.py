import mmap
import sys

usage = """
This program is used to convert a file to mmap

usage: python mmap.py filename

filename: file that you want to convert
"""

if len(sys.argv) < 2:
    print usage
    exit()

filename = sys.argv[1]

# Create mmap
f = open(filename, 'r+')
# memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print mm.readline()  # prints "Hello Python!"
# read content via slice notation
print mm.readline()  # prints "Hello Python!"

# close the map
mm.close()
