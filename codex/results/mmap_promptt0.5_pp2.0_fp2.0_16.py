import mmap
# Test mmap.mmap
# f = open('/home/jason/Documents/test.txt', 'r+b')
# m = mmap.mmap(f.fileno(), 0)
# m[0:11] = 'Hello World'
# m.close()
# f.close()

# Test mmap.mmap with mmap.ACCESS_READ
# f = open('/home/jason/Documents/test.txt', 'r+b')
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
# print m.readline()
# m.close()
# f.close()

# Test mmap.mmap with mmap.ACCESS_COPY
# f = open('/home/jason/Documents/test.txt', 'r+b')
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
# m[0:11] = 'Hello World'
# m.close()
# f.close()

# Test mmap.
