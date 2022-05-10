import select
# Test select.select()

# select.select() takes three lists as arguments:
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select.select() returns three lists corresponding to the first three arguments:
# rlist: sockets ready for reading
# wlist: sockets ready for writing
# xlist: sockets with an “exceptional condition”

# select.select() will block until at least one socket is ready.
# A socket is ready for reading if a recv() will not block.
# A socket is ready for writing if a send() will not block.

# select.select() can also be told to return after a fixed time via a 4th argument, timeout.
# If timeout is omitted the call will block until a socket is ready.
# If timeout is zero, the call will never block and will return three empty lists.
# If timeout is a positive number, the call will block for at most timeout seconds and may return three empty lists.

# select.select()
