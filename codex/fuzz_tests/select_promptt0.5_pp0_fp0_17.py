import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not supplied, will block if none of the lists are ready; if supplied as a number, will block that many seconds; if supplied as None, will never block, and return whatever is ready immediately
#
# Returns three lists corresponding to those passed in.
#
# Example:
#
# import select
# import socket
#
# s = socket.socket()
# s.bind(('', 8080))
# s.listen(5)
#
# while True:
#    r, w, x = select.select([s], [], [])
#    if s in r:
#        c, a = s.accept()
#        print c.recv(1024)
#        c.close()
#
# http://www.doughellmann.com/PyMOT
