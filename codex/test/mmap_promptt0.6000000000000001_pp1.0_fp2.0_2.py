import mmap
# Test mmap.mmap
# ---------------

m = mmap.mmap(0,1,None,mmap.ACCESS_READ)
m.close()

# Test mmap.mmap(-1,1,None,mmap.ACCESS_READ)
# ------------------------------------------

m = mmap.mmap(-1,1,None,mmap.ACCESS_READ)
m.close()

# Test mmap.mmap(1,1,None,mmap.ACCESS_READ)
# ----------------------------------------

# This should fail.
