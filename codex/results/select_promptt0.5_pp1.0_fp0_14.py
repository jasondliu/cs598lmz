import select
# Test select.select()
# http://docs.python.org/library/select.html
# http://www.doughellmann.com/PyMOTW/select/
# http://pymotw.com/2/select/

# select.select(rlist, wlist, xlist[, timeout])
# Monitor sockets for input and output readiness
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition"
# timeout: timeout in seconds

# The return value is a triple of lists of objects that are ready:
# (subset of rlist, subset of wlist, subset of xlist)

# The select function can be used to wake up a thread when a socket becomes
# ready for reading or writing.
# If a socket is in the read list and the remote end is closed, it will be
# returned in the exception list.

# If a socket is in the write list and the remote end is closed, it will be
# returned in the write list.

# If a socket is in the exception list, it will be returned in
