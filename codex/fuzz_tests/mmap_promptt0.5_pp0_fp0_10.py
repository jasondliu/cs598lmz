import mmap
# Test mmap.mmap

f = open('/home/jim/Downloads/test.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print m.readline()
print len(m)

# Test mmap.mmap

f = open('/home/jim/Downloads/test.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print m.readline()
print len(m)

# Test mmap.mmap

f = open('/home/jim/Downloads/test.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print m.readline()
print len(m)

# Test mmap.mmap

f = open('/home/jim/Downloads/test.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS
