import mmap
# Test mmap.mmap()
# Test buffering via mmap.mmap().read()
print "Testing read(1)"
s = mmap.mmap(-1, 100, "data")
s.write("completed")
s.seek(0)
print s.read(1)
print s.read(1)
print s.read(1)
print s.read(1)
print s.read(1)
print s.read(1)
print s.read(1)
print s.read(1)
print repr(s.read(1))
# Expect completed
print "Testing read(0)"
s = mmap.mmap(-1, 100, "data")
s.write("completed")
s.seek(0)
print s.read(0)
print repr(s.read(0))
# Expect completed
print "Testing readline()"
s = mmap.mmap(-1, 100, "data")
s.write("first\nsecond\nthird\nfourth\nfifth\n")
s.seek(0)
print s.readline()
print s
