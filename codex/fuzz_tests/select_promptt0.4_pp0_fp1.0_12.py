import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified or None, block until at least one file descriptor is ready;
# otherwise, block for at most timeout seconds and raise the exception if no file descriptor is ready during that time.
# Return value: three lists of objects that are ready

# import socket
# import select
#
# s = socket.socket()
# s.bind(('localhost',5000))
# s.listen(1)
#
# while True:
#     conn, addr = s.accept()
#     print('Connected by', addr)
#     while True:
#         data = conn.recv(1024)
#         if not data: break
#         conn.send(data)
#     conn.close()

# import socket
# import select
#
# s = socket.socket()
#
