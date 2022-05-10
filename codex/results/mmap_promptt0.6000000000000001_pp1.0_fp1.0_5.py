import mmap
# Test mmap.mmap
import mmap
f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print m.readline()
print m.readline()
print repr(m[0:10])
m.seek(0)
m[0:10] = 'L' * 10
m.close()
f.close()
# Test mmap.mmap
import mmap
f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print m.readline()
print m.readline()
print repr(m[0:10])
m.seek(0)
m[0:10] = 'L' * 10
m.close()
f.close()
# Test mmap.mmap
import mmap
f = open('lorem.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
print m.readline()
print m.readline()
print repr(m[0:10])
m.seek(
