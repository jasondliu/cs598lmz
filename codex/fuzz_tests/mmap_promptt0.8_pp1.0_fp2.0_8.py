import mmap
# Test mmap.mmap():
print("mmap.mmap(0, 1024) = %s" %repr(mmap.mmap(0, 1024)))
print("mmap.mmap(0, 1024, prot = mmap.PROT_READ) = %s" %repr(mmap.mmap(0, 1024, prot = mmap.PROT_READ)))
print("mmap.mmap(0, 1024, access = mmap.ACCESS_WRITE) = %s" %repr(mmap.mmap(0, 1024, access = mmap.ACCESS_WRITE)))
print("mmap.mmap(0, 1024, access = mmap.ACCESS_READ) = %s" %repr(mmap.mmap(0, 1024, access = mmap.ACCESS_READ)))
print("mmap.mmap(0, 1024, flags = mmap.MAP_SHARED) = %s" %repr(mmap.mmap(0, 1024, flags = mmap.MAP_SHARED)))
print("mmap.mmap(0, 1024, flags =
