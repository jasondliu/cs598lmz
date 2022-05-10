import mmap
# Test mmap.mmap(0, BUFSIZE)
BUFSIZE = 2048
f = open('testmmap', 'w+')
f.write('\0' * BUFSIZE)
f.close()
f = open('testmmap', 'r+')
m = mmap.mmap(f.fileno(), BUFSIZE)
print m[0:10]
print m[0]
m[0:11] = '0123456789'
m.flush()
m[0:11]
f.close()
m.close()
