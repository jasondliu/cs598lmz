import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# If the time out period value is omitted the function blocks until at least one file descriptor is ready.
# A time out value of zero specifies a poll and never blocks.

# The following example uses select() to implement a timeout:

# import socket
# import select
#
# def main():
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.setblocking(0)
#     s.connect(("www.python.org", 80))
#     while True:
#         ready = select.select([s], [], [], 5.0)
#         if ready[0]:
#             data = s.recv(1024)
#             break
#         else:

