import mmap
# Test mmap.mmap
# Do this first, before we run out of connections
data = mmap.mmap(conn.fileno(), 0, mmap.ACCESS_READ)
data[0:2] == b'\x01\x02'
# This is how you close an mmap'ed file
data.close()
# Make the connection unused
conn.close()
# Test mmap.mmap() over multiple pages.  The documentation
# doesn't say anything about this, but it seems to work.
# NOTE: This test depends on the previous test having run.
# NOTE: This test may fail with a SEGV on some systems.
# NOTE: This test depends on the page size being a power of 2.
#
# Also assumes that the test machine is a Unix or Linux system
# (other OSs have mmap but the semantics aren't necessarily the same)
#
# Also assumes that unlink() works the same way on the test OS
#
# Also assumes that the OS allows at least 64 processes to be
# running at the same time
#
# Also assumes that the OS doesn't limit the number of open file
#
