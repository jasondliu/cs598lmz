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
try:
    m = mmap.mmap(1,1,None,mmap.ACCESS_READ)
except mmap.error:
    pass
else:
    raise AssertionError, 'excepted mmap.error'

# Test mmap.mmap(0,0,None,mmap.ACCESS_READ)
# ----------------------------------------

# This should fail.
try:
    m = mmap.mmap(0,0,None,mmap.ACCESS_READ)
except mmap.error:
    pass
else
