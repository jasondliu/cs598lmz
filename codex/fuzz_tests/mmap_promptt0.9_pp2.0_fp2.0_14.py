import mmap
# Test mmap.mmap(-1)
illustrate(mmap.mmap(-1, 0))
illustrate(mmap.mmap(-1, 0))
illustrate(mmap.mmap(-1, 0))
illustrate(mmap.mmap(-1, 0))
# Test mmap.mmap(fd, 0)
illustrate(mmap.mmap(0, 0))
illustrate(mmap.mmap(1, 0))
illustrate(mmap.mmap(2, 0))
illustrate(mmap.mmap(3, 0))
# Test mmap.mmap(4294967295, 0)
illustrate(mmap.mmap(0xffffffff, 0))
illustrate(mmap.mmap(0xfffffffe, 0))
illustrate(mmap.mmap(0xfffffffd, 0))
illustrate(mmap.mmap(0xfffffffc, 0))
# Test mmap.mmap(-2) with a few pages at once
illustrate(mmap.mmap(-
