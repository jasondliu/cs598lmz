import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, especially over sockets.

# Example:
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.bind(('', 50007))
# >>> s.listen(1)
# >>> conn, addr = s.accept()
# >>> conn.recv(1024)
# 'Hello'
# >>> select.select([conn], [], [])
# ([<socket._socketobject object at 0x7f8f8e8e6b90>], [], [])
# >>> select.select([conn], [conn],
