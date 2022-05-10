import mmap
# Test mmap.mmap
# open file
fd = os.open('test.txt', os.O_RDWR)
# create mmap
m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
# write to mmap
m[0:6] = 'HELLO'
# close mmap
m.close()
# close fd
os.close(fd)

import mmap
# Test mmap.mmap
# open file
fd = os.open('test.txt', os.O_RDWR)
# create mmap
m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
# write to mmap
m[0:6] = 'HELLO'
# close mmap
m.close()
# close fd
os.close(fd)

import mmap
# Test mmap.mmap
# open file
fd = os.open('test.txt', os.O_RDWR)
# create mmap
m = mmap.mmap(fd, 0, access=mmap.
