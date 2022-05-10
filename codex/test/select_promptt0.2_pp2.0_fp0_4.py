import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output over a set of file descriptors.
# It can be used to implement a simple web server, for example.

# select.select() is also useful for implementing asynchronous I/O in Python.
# For example, if you want to wait for a socket to be readable and a file descriptor to be writable,
# you can do this:

# r, w, e = select.select([sock], [file], [], 10)
# if sock in r:
#     data = sock.recv(1024)
# if file in w:
#     file.write(data)
