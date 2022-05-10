import mmap
# Test mmap.mmap(fileno, length) constructor
BUFSIZE = 1024
fp = open('mmap_mmap_length.txt', 'w+')
