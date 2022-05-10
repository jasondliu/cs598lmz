import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified or None, block until at least one file descriptor is ready; otherwise, block for at most timeout seconds
#
# Return value:
# three lists of objects that are ready: subsets of the first three arguments

# We can use this function to wait for a socket to be ready for reading or writing.
# This can be used in a loop to wait for data to be available.

# Example:
#
# import socket
# import select
#
# s = socket.socket()
# s.bind(('localhost', 5000))
# s.listen(5)
#
# while True:
#     conn, addr = s.accept()
#     data = conn.recv(1024)
#     if not data:
#         break
#     conn.sendall(data
