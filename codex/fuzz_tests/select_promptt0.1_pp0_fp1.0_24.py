import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready

# select.select() is a useful way to multiplex input and output
# select.select() is a blocking call

# Example:
# select.select([sys.stdin], [], [], 0.0)[0]
# This will return a list containing sys.stdin if sys.stdin is ready for reading.
# If sys.stdin is not ready for reading, it will return an empty list.
# This is useful for checking whether there is input waiting to be read from sys.stdin.

# select.select() is also useful for implementing timeouts.
# For example, the following will wait up to one second for input on sys.stdin:
# ready =
