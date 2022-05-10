import mmap
# Test mmap.mmap()

# Open file
f = open('/home/matt/Desktop/Python/test.txt', 'r+')

# Memory-map the file, size 0 means whole file
mm = mmap.mmap(f.fileno(), 0)
