import mmap
# Test mmap.mmap by writing characters to a file using write() and reading
# them back using read().

import sys, mmap

filename = sys.argv[1]
f = open(filename, 'w+')
# writing 10 characters
f.write('0123456789')
m = mmap.mmap(f.fileno(), 10)
print 'Here is the file before read():', repr(m.read(10))
m.seek(0)
# reading 10 characters
print 'Here is the file after read():', repr(m.read(10))
m.seek(0)
# reading 5 characters
print 'Here is the file after read(5):', repr(m.read(5))
m.seek(0)
# reading no characters
print 'And the whole file:', repr(m.read())
m.close()
f.close()
