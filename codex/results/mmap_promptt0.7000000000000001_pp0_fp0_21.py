import mmap
# Test mmap.mmap for read-only access
m = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
print m.readline()
print m.readline()
m.close()

# Test mmap.mmap for read-write access
m = mmap.mmap(file.fileno(), 0)
print len(m)
m[0:11] = 'Hello world'
m.close()
print file.readline()
file.close()

# Test mmap() with length argument
file = open('mmap_file.txt', 'w+')
file.write('Hello world')
file.close()

with open('mmap_file.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 11)
    print len(m)
    m.close()

# Test mmap() with offset argument
with open('mmap_file.txt', 'r+') as f:
    m = mmap.mmap(f.fileno(), 11, offset=6)
    print
