import mmap
# Test mmap.mmap.tell
with open("foo.txt") as f:
  m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
