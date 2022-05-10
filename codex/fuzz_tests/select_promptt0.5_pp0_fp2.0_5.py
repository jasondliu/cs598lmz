import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist, wlist, xlist are lists of file descriptors to be monitored.
# Timeout is in seconds; it may be a float, or None to indicate no timeout

# select() returns three lists of file descriptors.
# The first list contains those descriptors that are ready for reading.
# The second list contains those descriptors that are ready for writing.
# The third list contains those descriptors that have an exceptional condition pending.

# The select() function is a useful interface to the underlying operating system
# select() call, but it does not offer a way to cancel a blocking select() call.
# For that, use the poll() function.

# select() can be used to monitor multiple file descriptors, waiting until one
# or more of the file descriptors become "ready" for some class of I/O operation
# (e.g., input possible).

# The first three arguments to select() are sequences of file descriptors to be
# watched. The first is the list of file descriptors to be watched for input; the

