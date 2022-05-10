import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.error: exception raised in case of an error

# select.select() can be interrupted by a signal (see the signal module)
# In that case, three empty lists are returned.

# select.select() is intended for I/O multiplexing.
# The first three arguments are sequences of ‘waitable objects’: either integers representing file descriptors or objects with a parameterless method named fileno() returning such an integer:

# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.fileno()
# 3
# >>> select.select([s], [], [])
# ([], [], [])
# >>>

# The optional timeout argument specifies a time-out as a floating point number
