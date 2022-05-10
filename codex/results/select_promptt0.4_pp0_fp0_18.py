import select
# Test select.select()

# Create a pair of connected sockets

# If timeout is > 0, select() blocks for at most timeout seconds.
# If timeout is 0, select() does not block at all, and returns
# immediately, even if no file descriptors are ready.
# If timeout is None, select() blocks until a file descriptor is ready.
# If a file descriptor becomes ready while select() is waiting,
# it will return immediately.

# select() returns three lists of file descriptors:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# On error, select() returns three empty lists.
# You can use select() to multiplex input from multiple sockets,
# but you can also use it to wait for a socket to be ready for reading or writing.

# The select() function is available on Unix and on Windows.
# On Unix, it supports devices, regular files, and pipes.
# On Windows, it supports sockets, regular files, and pipes.
# The
