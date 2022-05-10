import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sources.
# For example, you can use it to wait for input from both a network connection and standard input at the same time.

# Example:
# This example shows how to use select() to wait for input from stdin and a socket at the same time.
# It also shows how to use a timeout to avoid blocking indefinitely.

# The example uses a non-blocking socket, so it will work even if there is no input.
# If there is no input, it will print a message and exit.

# The example also shows how to use select() to monitor multiple sockets at the same
