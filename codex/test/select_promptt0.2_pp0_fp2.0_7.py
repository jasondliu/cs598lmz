import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until at least one file descriptor is ready; if specified as a float, will block that many seconds; if specified as None, will block indefinitely
#
# Returns three lists of objects that are ready: subsets of the first three arguments.
#
# Example:
#
# >>> import select
# >>> import socket
# >>> s = socket.socket()
# >>> s.connect(("www.python.org", 80))
# >>> s.send("GET / HTTP/1.0\r\n\r\n")
# >>> select.select([s], [], [], 5.0)
# ([<socket._socketobject object at 0x7f8b0f8f3b90>], [], [])
# >>> s.recv(1000)

