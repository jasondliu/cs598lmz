import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (not implemented on all platforms)

# Return value:
# three lists of objects that are ready: subset of the first three arguments

# Example:
# >>> import select
# >>> [i for i in dir(select) if '_' not in i]
# ['error', 'select', 'POLLERR', 'POLLHUP', 'POLLIN', 'POLLNVAL', 'POLLOUT', 'POLLPRI', 'POLLRDBAND', 'POLLRDNORM', 'POLLWRBAND', 'POLLWRNORM']
# >>> select.select([], [], [], 10)
# ([], [], [])
# >>> select.select([], [], [], 1)
# ([], [], [])
# >>> select.select([], [], [], 0)
# ([], [], [])
# >>> select.
