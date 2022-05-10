import mmap
# Test mmap.mmap

mm = mmap.mmap(descriptor, len, access=None)
mm[:] = 'x' * size   # write
mm[1:10:2] = 'ABCD'  # slice assignment
mm[1]           # returns bytes object with single character
mm.read_byte()
mm.readline()
mm.readline(10)
len(mm)
mm.tell()
mm.seek(pos, whence=0)
mm.close()
mm.find(b'pattern')
# Test mmap.ACCESS_*

mmap.ACCESS_DEFAULT
mmap.ACCESS_READ
mmap.ACCESS_COPY
mmap.ACCESS_WRITE
mmap.ACCESS_EXECUTE
# Test mmap.MAP_*

mmap.MAP_PRIVATE
mmap.MAP_SHARED
mmap.MAP_FIXED
mmap.MAP_ANONYMOUS
mmap.MAP_ANON
mmap.MAP_GROWSDOWN
mmap.MAP_DENYWRITE
