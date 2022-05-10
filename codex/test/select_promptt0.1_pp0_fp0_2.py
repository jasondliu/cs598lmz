import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, especially when there are many connections to monitor.

# Example:
# import socket
# import select
#
# s = socket.socket()
# s.bind(('localhost', 5000))
# s.listen(5)
#
# inputs = [s]
#
# while True:
#     rs, ws, es = select.select(inputs, [], [])
#     for r in rs:
#         if r is s:
#             c, addr = s.accept()
#             print 'Got connection from', addr
#             inputs
