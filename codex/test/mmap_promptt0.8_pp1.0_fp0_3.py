import mmap
# Test mmap.mmap, mmap.ACCESS_COPY
with open("lorem.txt", "r+b") as f:
  mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)
  print('First 10 bytes via read :', mm.read(10))
  print('First 10 bytes via slice:', mm[:10])
  print('2nd   10 bytes via read :', mm.read(10))
  mm.seek(0)
  print('First 10 bytes via read :', mm.read(10))


# Test mmap.mmap, mmap.ACCESS_DEFAULT
with open("lorem.txt", "r+b") as f:
  mm = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_DEFAULT)
  print('First 10 bytes via read :', mm.read(10))
  print('First 10 bytes via slice:', mm[:10], '\n')
  mm[0] = b'J'
  mm.flush()
  mm.seek
