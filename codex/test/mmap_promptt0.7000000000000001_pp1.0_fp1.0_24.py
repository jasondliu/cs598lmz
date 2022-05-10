import mmap
# Test mmap.mmap class

# memory map an existing file
f = open('tmp', 'w+')
f.write('Hello World\n')
f.close()

# open for reading and writing
f = open('tmp', 'r+')
# memory-map the file, size 0 means whole file
