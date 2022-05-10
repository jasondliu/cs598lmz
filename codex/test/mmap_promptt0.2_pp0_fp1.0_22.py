import mmap
# Test mmap.mmap(0,1)
# This is a test for http://bugs.python.org/issue1074397
# It will simply map a byte of memory and then access it.
# If it segfaults, you're in trouble.

with open("/dev/zero", "rb") as f:
    m = mmap.mmap(f.fileno(), 1, access=mmap.ACCESS_READ)
    print(m[0])
