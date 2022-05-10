import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, it specifies a timeout in seconds (float) and the function will return three lists after that time if no file descriptors became ready

# Return value: three lists of file descriptors: rlist, wlist, xlist

# Example:
# import select
# import socket
#
# s = socket.socket()
# s.bind(('localhost', 5000))
# s.listen(1)
#
# conn, addr = s.accept()
#
# while True:
#     r, w, x = select.select([conn], [], [])
#     if r:
#         data = conn.recv(1024)
#
