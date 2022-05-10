import mmap
# Test mmap.mmap

# f = open('test.txt', 'r+')
# m = mmap.mmap(f.fileno(), 0)
# # m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
# print m[:]
# print len(m)
# m.close()
# f.close()

# # Test mmap.mmap with mmap.ACCESS_WRITE
# f = open('test.txt', 'r+')
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
# print m[:]
# print len(m)
# m.close()
# f.close()

# Test mmap.mmap with mmap.ACCESS_COPY
f = open('test.txt', 'r+')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
print m[:]
print len(m)
m.close()
f.close()
