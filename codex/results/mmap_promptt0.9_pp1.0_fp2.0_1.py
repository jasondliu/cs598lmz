import mmap
# Test mmap.mmap(fileno, length) constructor
BUFSIZE = 1024
fp = open('mmap_mmap_length.txt', 'w+')
try:
    n = mmap.mmap(fp.fileno(), BUFSIZE)
    print n.size()
finally:
    n.close()
    fp.close()

# Test mmap.mmap(fileno, length, access=ACCESS_READ)
fp = open('mmap_mmap_length_access.txt', 'w+')
try:
    n = mmap.mmap(fp.fileno(), BUFSIZE, mmap.ACCESS_READ)
    print n.size()
finally:
    n.close()
    fp.close()
</code>
I'm getting an AttributeError, saying "mmap has no attribute 'ACCESS_READ'."  Why is mmap giving me this error?  It's pretty much straight from the documentation.


A:

You are using Python 2.3, which has a completely different mmap module than 2.4+. Please consult the new-style mm
