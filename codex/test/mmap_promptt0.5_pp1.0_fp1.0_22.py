import mmap
# Test mmap.mmap().
with open("/proc/self/maps", "r") as f:
  m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
  print(m.readline())
  print(m.readline())
  print(m.readline())
  print(m.readline())
  m.close()

# Test mmap.mmap(fd, length).
with open("/proc/self/maps", "r") as f:
  m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
  print(m.readline())
