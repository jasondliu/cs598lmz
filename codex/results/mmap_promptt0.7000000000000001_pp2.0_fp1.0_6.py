import mmap
# Test mmap.mmap

try:
    f = open('/etc/fstab', 'r')
except IOError:
    print 'cannot open file'
else:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print mm.readline()
    mm.close()
    f.close()

# Test mmap.mmap.move

try:
    f = open('/etc/fstab', 'r')
except IOError:
    print 'cannot open file'
else:
    mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print mm.readline()
    mm.move(0, 0, 10)
    print mm.readline()
    mm.close()
    f.close()

# Test mmap.mmap.find

try:
    f = open('/etc/fstab', 'r')
except IOError:
    print 'cannot open file'
else:
    mm = mmap.mmap(f
