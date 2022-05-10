import mmap
# Test mmap.mmap by writing characters to a file using write() and reading
# them back using read().

import sys, mmap

filename = sys.argv[1]
f = open(filename, 'w+')
# writing 10 characters
f.write('0123456789')
m = mmap.mmap(f.fileno(), 10)
