import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: wait for a specified time in seconds, or until a file descriptor is ready

# Returns three lists of objects that are ready: subsets of the first three arguments.

# When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

import socket
import select

def test_select():
    s = socket.socket()
    s.setblocking(0)
    s.bind(('127.0.0.1', 5000))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr

    while 1:
        ready = select.select([s], [], [], 2)
        if ready[0]:
            data = conn.recv(1024)
            if not data: break
            conn
