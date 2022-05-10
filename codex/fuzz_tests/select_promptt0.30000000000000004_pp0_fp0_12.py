import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block for at least that long

# Return value: three lists of objects that are ready: subsets of the first three arguments
# If the time-out is reached without a file descriptor becoming ready, three empty lists are returned

# Example:
# >>> import select
# >>> select.select([], [], [], 5.0)
# ([], [], [])
# >>>

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.setblocking(0)
# >>> select.select([s], [], [], 5.0)
# ([], [], [])
# >>>

# Example:
# >>> import select
