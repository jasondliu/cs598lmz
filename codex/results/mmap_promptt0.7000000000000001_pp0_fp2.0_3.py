import mmap
# Test mmap.mmap.read
m = mmap.mmap(0, 8, "testmmap", mmap.ACCESS_READ)
if m.read(8) != "12345678":
    print "Bad read"
m.close()

# Test mmap.mmap.read_byte
m = mmap.mmap(0, 8, "testmmap", mmap.ACCESS_READ)
if m.read_byte() != ord('1'):
    print "Bad read"
m.close()

# Test mmap.mmap.readline
m = mmap.mmap(0, 8, "testmmap", mmap.ACCESS_READ)
if m.readline() != "12345678":
    print "Bad read"
m.close()

# Test mmap.mmap.readline
m = mmap.mmap(0, 10, "testmmap", mmap.ACCESS_READ)
if m.readline() != "12345678\n9\n":
    print "Bad read"
m.close()

# Test mm
