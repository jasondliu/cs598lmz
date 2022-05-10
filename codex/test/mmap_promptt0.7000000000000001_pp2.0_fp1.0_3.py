import mmap
# Test mmap.mmap(0, BUFSIZE)
BUFSIZE = 2048
f = open('testmmap', 'w+')
f.write('\0' * BUFSIZE)
f.close()
f = open('testmmap', 'r+')
m = mmap.mmap(f.fileno(), BUFSIZE)
