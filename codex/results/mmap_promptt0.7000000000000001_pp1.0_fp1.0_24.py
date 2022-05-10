import mmap
# Test mmap.mmap class

# memory map an existing file
f = open('tmp', 'w+')
f.write('Hello World\n')
f.close()

# open for reading and writing
f = open('tmp', 'r+')
# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print "Memory map:", m.readline(), 

# read content via slice notation
print m[:5]

# update content using slice notation;
# note that new content must have same size
m[6:] = 'world'
# ... and read again using standard file methods
m.seek(0)
print "Memory map:", m.readline(), 

# close the map
m.close()

# close the file
f.close()

# Test mmap.mmap class, offset and size

# memory map an existing file
f = open('tmp', 'w+')
f.write('Hello World\n')
f.close()

# open for reading and writing
