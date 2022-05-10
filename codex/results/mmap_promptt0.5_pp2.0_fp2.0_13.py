import mmap
# Test mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE)
# This should give an error on Windows, and succeed on UNIX.
# On UNIX, it should map an anonymous page, not one backed by the
# filesystem.
#
# The test is skipped if mmap.mmap(-1, 0, access=mmap.ACCESS_WRITE) fails
# with ENODEV.
#
# This test was written to check that a bug in mmap.mmap(-1, 0,
# access=mmap.ACCESS_WRITE) on Windows was fixed.
import os, sys

try:
    fd = os.open('/dev/zero', os.O_RDWR)
except (IOError, OSError):
    fd = os.open('/dev/null', os.O_RDWR)

m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
if sys.platform == 'win32' and m.size() != 0:
    raise RuntimeError('mmap.mmap(-1, 0,
