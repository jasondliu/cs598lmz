import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() can be used as a way to implement a timeout on blocking I/O operations like socket.accept() or socket.recv().

# The following example uses select() to implement a timeout on a blocking accept() call:

import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 5000))
s.listen(1)

# Wait for at most 5 seconds for a connection
timeout = 5
ready = select.select([s], [], [], timeout)
if ready[0]:
    # Socket is readable, accept the connection
    connection, address = s.accept()
else:
    # No connection within timeout period
    print
