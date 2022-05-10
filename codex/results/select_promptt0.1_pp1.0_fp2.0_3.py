import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output access to many file descriptors in a program with a small number of OS threads.

# select.select() is also useful for handling sockets.

# select.select() is available on Unix and on Windows.

# select.select() monitors sockets, open files, and pipes (anything with a fileno() method that returns a valid file descriptor) until they become readable or writable or a communication error occurs.

# select.select() is a useful way to multiplex input/output access to many file descriptors in a program with a small number of OS threads.

# select.select() is
