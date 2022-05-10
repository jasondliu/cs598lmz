import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# Timeout is in seconds; can be a float. If None, will block until a monitored file descriptor becomes ready.

# select() is a useful way to multiplex input/output over a number of sockets or other file objects.

# select() supports sockets, pipes, and files on most platforms.

# select() is the most portable way to do this.

# select() is available on Unix and on Windows.

# select() is a useful way to multiplex input/output over a number of sockets or other file objects.

# select() supports sockets, pipes, and files on most platforms.

# select() is the most portable way to do this.

# select() is available on Unix and on Windows.

# select() is a useful way to
