import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output access to many file descriptors in a program with many threads.

# select.select() is also useful for handling sockets.

# select.select() is also useful for handling pipes.

# select.select() is also useful for handling regular files.

# select.select() is also useful for handling devices.

# select.select() is also useful for handling FIFOs.

# select.select() is also useful for handling terminals.

# select.select() is also useful for handling pseudo-terminals.

# select.select() is also useful for handling sockets.
