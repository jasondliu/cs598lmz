import mmap
# Test mmap.mmap mapping size limit
#
# This test case tests that mmap can map files above the 2 GB
# limit.  On Win32, the limit is 4 GB.  On other platforms,
# mmap has a limit of sys.maxint.

if sys.platform.startswith("win"):
    limit = 4 * 1024 * 1024 * 1024
else:
    limit = sys.maxint

with open("data.dat", "wb") as f:
    f.seek(limit)
    f.write("\0")
    f.flush()

with open("data.dat", "rb") as f:
    m = mmap.mmap(f.fileno(), 0)
    m[limit-1] = "A"

m.close()
