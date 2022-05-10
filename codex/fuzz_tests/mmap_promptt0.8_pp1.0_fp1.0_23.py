import mmap
# Test mmap.mmap() without len = 0
m = mmap.mmap(-1, 0)

# Test mmap.mmap(fileno)
f = open("testfile", "w+")
f.write("Hello Python!\n")
f.flush()
m = mmap.mmap(f.fileno(), 0)
str = m.readline()
print "Read Line: " + str.strip()

# Test mmap.mmap(fileno, length)
f = open("testfile", "w+")
f.write("Hello Python!\n")
f.flush()
m = mmap.mmap(f.fileno(), 13)
print "Start: %s, length: %s, size: %s" % (m.tell(), m.size( ), len(m))
print "Before: %s" % m.readline( )

# Test mmap.mmap(fileno, length, access, offset)
f = open("testfile", "w+")
f.write("Hello Python!\n")
f.flush()
m = mmap.
