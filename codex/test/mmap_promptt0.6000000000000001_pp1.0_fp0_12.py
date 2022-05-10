import mmap
# Test mmap.mmap

# open file
f = open("test/test.txt", "r+")

# memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

# read content via standard file methods
