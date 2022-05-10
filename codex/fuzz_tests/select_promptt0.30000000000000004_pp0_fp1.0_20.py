import select
# Test select.select()
# select.select() is a blocking call, it will wait until the file descriptor
# is ready for I/O.

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, select() can block indefinitely, otherwise it will block for at most timeout seconds

# select.select() returns three lists of file descriptors:
# rlist: those sockets ready for reading
# wlist: those sockets ready for writing
# xlist: those sockets with exceptions

# select.select() will return three empty lists if the timeout is reached

# select.select() is available on all platforms (Windows, Linux, Mac OS X, etc.)

# The following example will wait until a socket is ready for reading, or until a second has passed:

import socket
import select

s = socket.socket()

# set blocking to 0, so .recv() will
