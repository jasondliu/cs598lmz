import mmap
# Test mmap.mmap.readline()

# Open a file and write some text to it
f = open('test.txt', 'w+')
f.write('\x00' * 1024)

# Memory-map the file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)

