import mmap
# Test mmap.mmap() and os.fdopen() performance.
fd = os.open("/dev/zero", os.O_RDONLY)
byte = mmap.mmap(fd, 0, mmap.MAP_SHARED, mmap.PROT_READ)
# Measure mmap.mmap() performance.
start = time.time()
byte.read(1)
end = time.time()
mmap_time = end - start

# Measure os.fdopen() performance.
fd = os.open("/dev/zero", os.O_RDONLY)
start = time.time()
byte = os.read(fd, 1)
end = time.time()
os_time = end - start

# Print performance difference.
factor = os_time / mmap_time
print("os: %s" % os_time)
print("mmap: %s" % mmap_time)
print("mmap is %s faster" % factor)
