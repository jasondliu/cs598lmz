import mmap
# Test mmap.mmap(0, 1024)
print(mmap.mmap(0, 1024))
# Test mmap.mmap(0, 1024, mmap.MAP_SHARED)
print(mmap.mmap(0, 1024, mmap.MAP_SHARED))
# Test mmap.mmap(0, 1024, mmap.MAP_SHARED, mmap.PROT_READ)
print(mmap.mmap(0, 1024, mmap.MAP_SHARED, mmap.PROT_READ))
# Test mmap.mmap(0, 1024, mmap.MAP_SHARED, mmap.PROT_READ, mmap.ACCESS_READ)
print(mmap.mmap(0, 1024, mmap.MAP_SHARED, mmap.PROT_READ, mmap.ACCESS_READ))
# Test mmap.mmap(0, 1024, mmap.MAP_SHARED, mmap.PROT_READ, mmap.ACCESS_READ, 0)
print(mmap.mmap(0, 1024, mmap.MAP
