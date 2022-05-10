import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select.select() can be used as a way to implement a timeout on blocking I/O operations like socket.accept() and socket.recv().
# The following example uses select() to implement a timeout on a blocking accept() call:

import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50007))
s.listen(1)

sock, addr = s.accept()

print("Connection from:", addr)

while True:
    rl, wl, xl = select.select([sock], [], [], 5)
    if len(rl) > 0:
        # Receive bytes and convert them to a string
