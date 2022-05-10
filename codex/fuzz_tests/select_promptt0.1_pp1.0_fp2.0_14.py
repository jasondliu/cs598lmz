import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input/output over a number of sockets or other file-like objects.
# It can be used to wait for a socket to become readable, writable or have an exceptional condition.

# select.select() is available on all platforms that support the select() system call.
# On Windows, it only works for sockets; on Unix, it also works for other file types (in particular, on Unix,
# it works on pipes).

# select.select() can be used to wait for a socket to become readable, writable or have an exceptional condition.
# The first three arguments are sequences of socket objects.
#
