import mmap
# Test mmap.mmap() function

import os
import mmap

# create a file
f = open('/Users/mike/Desktop/test.txt', 'w')

f.write('Hello World')

f.close()

# open the file in read-only mode
f = open('/Users/mike/Desktop/test.txt', 'r')

# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)

# read content via standard file methods
print('m[:]   :', m[:])
print('m.read():', m.read(11))

# close the map
m.close()

# close the file
f.close()
# Test mmap.mmap() function

import os
import mmap

# create a file
f = open('/Users/mike/Desktop/test.txt', 'w')

f.write('Hello World')
