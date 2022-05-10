import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output over a set of sockets.

# Example:
# import socket
# import select
#
# s = socket.socket()
# s.bind(('', 50007))
# s.listen(1)
#
# conn, addr = s.accept()
# print 'Connected by', addr
#
# while 1:
#     ready = select.select([conn], [], [], 1)
#     if ready[0]:
#         data = conn.recv(1024)
#         if not data: break
#         conn.send(data)
