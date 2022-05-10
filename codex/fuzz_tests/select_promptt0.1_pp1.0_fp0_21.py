import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input/output over a number of sockets or other file-like objects.

# The following example shows how to use select.select() to monitor a number of sockets (including standard input) for activity.

# The example is written for sockets, but it can be used for any file-like object (for example, serial ports and pipes).

# The example also illustrates the use of the optional timeout parameter to select(). If no timeout is supplied, select() can block indefinitely.

# The example is runnable, but it will do nothing unless standard input is redirected to a file or piped from another process.

#!/usr/bin/env python
