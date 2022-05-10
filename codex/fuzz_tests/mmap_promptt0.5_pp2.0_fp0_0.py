import mmap
# Test mmap.mmap(-1, 1)

import mmap

m = mmap.mmap(-1, 1)
m.close()

# Test mmap.mmap(fd, 0)

import mmap

m = mmap.mmap(0, 0)
m.close()

# Test mmap.mmap(fd, 0, access=mmap.ACCESS_READ)

import mmap

m = mmap.mmap(0, 0, access=mmap.ACCESS_READ)
m.close()

# Test mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)

import mmap

m = mmap.mmap(0, 0, access=mmap.ACCESS_WRITE)
m.close()

# Test mmap.mmap(fd, 0, access=mmap.ACCESS_COPY)

import mmap

m = mmap.mmap(0, 0, access=mmap.ACCESS_COPY)
m.close()

# Test mmap.mm
