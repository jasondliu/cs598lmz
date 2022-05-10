import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])

# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# timeout is a floating point number specifying a timeout for the operation in seconds (or fractions thereof).
# If timeout is omitted the call blocks until at least one file descriptor is ready.
# A timeout of zero specifies a poll and never blocks.

# Returns three lists of objects that are ready:
# rlist -- sequence of objects that are ready for reading
# wlist -- sequence of objects that are ready for writing
# xlist -- sequence of objects that have an “exceptional condition”

# If the time-out is reached without a file descriptor becoming ready,
# three empty lists are returned.
# Exceptions are the same as those for the poll() function above.

# On Windows, only sockets are supported; on Unix, all file descriptors.

# Example:
# >>> import socket
# >>> import select
# >>>
