import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, for example, when you have a user interface with multiple input sources (keyboard, mouse, ...) and multiple output sinks (graphics display, printer port, ...).

# select.select() can also be used to monitor multiple sockets for incoming data and, in general, to multiplex input and output among multiple channels.

# select.select() is also useful when you want to implement a timeout for socket operations.

# select.select() is available on Unix and on Windows.

# select.select() is not available on the Macintosh, because the Macintosh does not support select() at the operating system
