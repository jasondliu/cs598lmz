import mmap
# Test mmap.mmap
# open a file
f = open('/tmp/test.txt', 'r+')
# memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
