import mmap
# Test mmap.mmap

f = open('test.txt', 'r+')
# memory-map the file, size 0 means whole file
map = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
