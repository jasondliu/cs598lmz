import mmap
# Test mmap.mmap(..)
#f = open("temp.data", "r+b")
#m = mmap.mmap(f.fileno(), 0)
#print repr(m[:])
#f.close()

# Test mmap.mmap(fileno, ...)
#f = open("temp.data", "w+b")
#f.write('\x00')*1024
#m = mmap.mmap(f.fileno(), 1024)
#m[0] = 'a'
#print repr(m[0])
#print repr(m[1])
#print repr(m[2])
#f.close()

# Test mmap.mmap(-1, ..)
#m = mmap.mmap(-1, 1024, access = mmap.ACCESS_READ)
#assert m
#m.close()

# Test mmap.mmap(0, ..)
#m = mmap.mmap(0, 1024, access = mmap.ACCESS_READ)
#assert m
#m.close()

# Test mmap.
