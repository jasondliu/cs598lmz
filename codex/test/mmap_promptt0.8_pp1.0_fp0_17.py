import mmap
# Test mmap.mmap(2)
#m = mmap.mmap(-1, 65536) # 1 page
# Test mmap.mmap(3)
m = mmap.mmap(-1, 65536, "test.mmap.py") # 1 page
# Test mmap.mmap(4)
#m = mmap.mmap(-1, 65536, "test.mmap.py", mmap.PROT_READ|mmap.PROT_WRITE) # 1 page

