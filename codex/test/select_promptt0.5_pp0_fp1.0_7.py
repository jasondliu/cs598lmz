import select
# Test select.select() with a file descriptor that is greater than the
# highest file descriptor known to the kernel.

import os
import errno
import select

# Find the largest file descriptor.
maxfd = os.sysconf("SC_OPEN_MAX")
if maxfd == -1:
    maxfd = 256

# Create a pipe and find its read end.
r, w = os.pipe()

# Close all file descriptors.
os.closerange(0, maxfd)

# Open a file descriptor that is larger than the pipe's read end.
fd = os.open(__file__, os.O_RDONLY)
try:
    # Try to select on the pipe's read end.
    rlist, wlist, xlist = select.select([r], [], [], 1)
except select.error as e:
    if e.args[0] != errno.EBADF:
        raise
else:
    raise AssertionError("select.select() didn't raise EBADF")
finally:
    os.close(fd)
