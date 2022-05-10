import mmap
# Test mmap.mmap()
# - create 4GiB sparse file
# - mmap() with MAP_POPULATE, read/write all pages with
#   random offsets and comparing memory contents
f = open('/tmp/goxnet/xxcntrmmap', 'w+')
f.truncate(1024*1024*1024*4)
f.close()

# Repeat test 10 times
for t in range(10):
  f = open('/tmp/goxnet/xxcntrmmap', 'r+')
  m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)

  map_sz = m.size() / mmap.PAGESIZE
  print("mapping %d pages (size=%d)" % (map_sz, m.size()))
  m.resize(m.size() + len("."))
  m.flush()

  #for idx in range(0, map_sz, 64):
  while map_sz > 0:
    #print("  idx=%d
