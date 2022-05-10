import mmap
# Test mmap.mmap create
mapped = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
mapped.resize(6*mmap.ALLOCATIONGRAIN)
mapped.write(b'12345')
