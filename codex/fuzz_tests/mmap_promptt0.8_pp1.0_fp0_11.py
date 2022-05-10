import mmap
# Test mmap.mmap()
# This gets us an mmap instance
m = mmap.mmap(0, 1024)
# A plain old str, not a unicode
s = "Hello, World!\n"
print "Before:", repr(m.readline())
# Get the size of the string
m.write(s)
print "After:", repr(m.readline())

# Test mmap.mmap()
# This gets us an mmap instance
m = mmap.mmap(1, 1024, access=mmap.ACCESS_WRITE)
# A plain old str, not a unicode
s = "Hello, World!\n"
print "Before:", repr(m.readline())
# Get the size of the string
m.write(s)
print "After:", repr(m.readline())

# Test mmap.mmap()
# This gets us an mmap instance
m = mmap.mmap(1, 1024, access=mmap.ACCESS_READ)
# A plain old str, not a unicode
s = "Hello, World!\n
