import mmap
# Test mmap.mmap
print(mmap.mmap(-1, 10))
print(mmap.mmap(-1, 10, prot=mmap.PROT_READ))
print(mmap.mmap(-1, 10, flags=mmap.MAP_SHARED, prot=mmap.PROT_READ))
print(mmap.mmap(-1, 10, flags=mmap.MAP_SHARED, prot=mmap.PROT_READ, access=mmap.ACCESS_READ))

# Test mmap.mmap.__getitem__
m = mmap.mmap(0, 10)
m[0]
m[0:1]
m[0:1:1]
m[0:1:2]
m[0:10:2]
m[0:10:1]
m[0:10:2]
m[0:10:3]
m[0:10:4]
m[0:10:5]
m[0:10:6]
m[0:10:7]
m[0:10:8]
m[
