import mmap
# Test mmap.mmap size limits
#
# Create a 1MB zeroed mmap, then write a bunch of strings to it, until we
# get an exception.  On systems with large virtual memory, this should
# produce a NegativeSizedException; but on systems where address space
# is limited, we should get a MemoryError.

MMAP_SIZE = 1024 * 1024
MAP_ANONYMOUS = -1

def test1():
    fd = os.open('/dev/zero', os.O_RDWR)
    buf = mmap.mmap(fd, MMAP_SIZE, access=mmap.ACCESS_WRITE)
    os.close(fd)

    if sys.maxsize < (1<<32):
        # On 32-bit systems, we can't allocate 1MB
        expect_exception = (MemoryError, NegativeSizedException)
    else:
        expect_exception = (MemoryError,)

    i = 0
    while True:
        try:
            buf[i:i+1] = bytes((i, ))
        except expect_exception:
            break
        i
