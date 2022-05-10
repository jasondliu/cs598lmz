import mmap
# Test mmap.mmap
# ===========================================================

import os,sys,mmap

def mapcopy(frm, to, sz):
    m1 = mmap.mmap(frm.fileno(), sz, access=mmap.ACCESS_READ)
    if not hasattr(to, "write"): # check for file-like object
        to = open(to, "wb")
    m2 = mmap.mmap(to.fileno(), sz, access=mmap.ACCESS_WRITE)
    m2[:] = m1
    m2,m2 = None, None # close twice, because windows

if __name__ == "__main__":
    f = open("test_mmap", "r+")
    f.write("\x00" * os.path.getsize("test_mmap"))
    mapcopy("test_mmap", sys.stdout, os.path.getsize("test_mmap"))
    f.seek(0)

# Test mmap.mmap
# ===========================================================

