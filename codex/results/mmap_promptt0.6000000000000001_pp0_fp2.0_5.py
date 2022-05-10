import mmap
# Test mmap.mmap
#import mmap
#f = open("../data/test_mmap.txt", "r+b") # r+b: read-write binary mode
#m = mmap.mmap(f.fileno(), 0)
#print len(m)
#print m[0:10]
#print m[0]
#print m[0:1]
#m[0:11] = "Hello Python"
#m.close()
#f.close()

# Test mmap.mmap(fileno, length, mmap_mode)
import mmap
f = open("../data/test_mmap_mode.txt", "w+b")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
m.write("Hello Python")
m.close()
f.close()

f = open("../data/test_mmap_mode.txt", "r+b")
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print m[:]
