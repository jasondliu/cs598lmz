import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block for at least that many seconds (can be a float)

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input from multiple sources.

# Example:

# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('localhost', 5000))
# >>> s.listen(1)
# >>> s.setblocking(0)
# >>> while True:
# ...     ready = select.select([s], [], [], 5.0)
# ...     if ready[0]:
# ...         client, addr = s.accept()
