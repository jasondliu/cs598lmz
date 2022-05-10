import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# return value: three lists of objects that are ready

# timeout: if omitted (or if timeout is None), block until at least one file descriptor is ready
# if timeout is a float, it specifies a timeout (in seconds) for the operation
# if timeout is 0.0, return immediately even if no file descriptors are ready

# select() never “reports” an error in the file descriptors you pass in, except for out-of-range file descriptor values
# if select() returns three empty lists, this means that the timeout has expired before anything interesting happened

# select() is a useful way to multiplex input/output over sockets and other file-like objects
# it can be used to wait for a socket to become readable/writable/exceptional
# it can also be used to wait for a file descriptor to become readable
