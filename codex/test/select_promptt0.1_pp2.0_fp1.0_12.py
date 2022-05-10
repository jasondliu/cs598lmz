import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input/output over a set of file descriptors.
# It can be used to implement a simple network server.

# Example:
# The following example shows how to use select() to monitor a set of sockets and connections for data available for reading.
# It also shows how to use select() to monitor a single socket for space to write data.

# The example is a simple echo server that listens on port 50007 and echoes back whatever it receives.
# It uses select() to handle multiple connections simultaneously.

# The example is written for Python 3.
# It also works under Python 2.7, but the code is slightly different.

