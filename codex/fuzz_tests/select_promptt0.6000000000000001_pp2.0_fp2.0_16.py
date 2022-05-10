import select
# Test select.select function
# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist are lists of file descriptors to be checked.
# timeout is an optional integer timeout in milliseconds.
# The return value is a triple of lists of objects that are ready.
# The first list contains those objects that are ready for reading,
# the second contains those that are ready for writing,
# and the third contains those that have raised exceptions.
# A file descriptor is ready for reading if it may be read without blocking.
# A file descriptor is ready for writing if writing will not block.
# If a timeout is given and no file descriptor is ready,
# the function will block for at most timeout milliseconds.
# If a timeout is given and at least one file descriptor is ready,
# the function will block for at most timeout milliseconds.
# If a timeout is not given, the function will block until at least one file descriptor is ready.

# Example:
# rlist, wlist, xlist = select.select([sys.stdin], [], [], 0.1)
# This blocks waiting for input on sys.
