import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, for example, when you have a server that handles multiple clients at the same time.

# Example:

# import socket
# import select

# s = socket.socket()
# host = socket.gethostname()
# port = 1234
# s.bind((host, port))

# s.listen(5)
# input = [s]

# while True:
#     inputready, outputready, exceptready = select.select(input, [], [])

#     for s in inputready:

#         if s == server:
