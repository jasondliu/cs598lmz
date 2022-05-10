import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: wait until a timeout occurs

# The return value is a triple of lists of objects that are ready:
# (subset of rlist, subset of wlist, subset of xlist)

# select() uses a very efficient algorithm to perform this task.
# It’s not uncommon to wait on a large number of sockets.
# A naive implementation would need to check each socket to see if it was ready.
# The select() function only checks sockets that are ready.
# select() returns the sockets that are ready.

# It is possible for an object to be removed from an fd list after
# it has been selected.
# This can happen, for example, if one of the objects in the
# write list has a buffer that fills up.
# In this case, the object must be removed from the write list
