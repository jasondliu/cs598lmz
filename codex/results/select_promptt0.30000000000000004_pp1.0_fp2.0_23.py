import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: a time-out as a floating point number in seconds (or None for no time-out)
# Return value: three lists of objects that are ready

# Example:
# >>> import sys, select
# >>> from socket import socket, AF_INET, SOCK_STREAM
# >>> s = socket(AF_INET, SOCK_STREAM)
# >>> s.connect(('localhost', 20000))
# >>> s.send(b'Hello')
# 5
# >>> select.select([s], [], [], 1.0)
# ([<socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 53370)>], [], [],
