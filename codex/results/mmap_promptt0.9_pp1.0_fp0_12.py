import mmap
# Test mmap.mmap()
###############################################################

a = mmap.mmap(0, 1, "", mmap.ACCESS_READ)
assert a.find("\0")!=-1, "Could not find end of file"
assert a.rfind("\0")!=-1, "Could not find end of file"

a = mmap.mmap(0, 1, "", mmap.ACCESS_WRITE)
a[0] = "a"

a = mmap.mmap(-1, 1, "", mmap.ACCESS_WRITE)
assert a[0] == "\0", "First byte is not null"

# Note here the size is ignored
a = mmap.mmap(-1, 0, "", mmap.ACCESS_WRITE)
assert a[0] == "\0", "First byte is not null"

a.close()
print "OK"
