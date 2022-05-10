import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input and output,
# allowing your program to monitor many file descriptors at once and respond appropriately when one or more of them is “ready” for some class of I/O operation.

# select.select() is available on Unix and Windows systems.

# select.select() is a useful way to multiplex input and output,
# allowing your program to monitor many file descriptors at once and respond appropriately when one or more of them is “ready” for some class of I/O operation.

# select.select() is available on Unix and Windows systems.

# select.select() is a useful way to multiplex input and
