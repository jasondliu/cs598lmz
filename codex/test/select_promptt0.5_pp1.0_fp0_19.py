import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])

# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# select() can be told to wait forever by passing None as the timeout value.
# If no descriptors are ready, select() will block until at least one is ready;
# if timeout is a non-negative integer or None then it will block at most timeout seconds and
# will always return at least one descriptor (possibly more, if descriptors become ready while select() is waiting).
# If timeout is a positive floating point number then the maximum wait time will be timeout seconds (or until a descriptor becomes ready, if that happens first).

# Return value is a triple of lists of objects that are ready: sublists corresponding to the three arguments of select()
# (which, in turn, correspond to the three arguments of select()).

# The optional timeout argument specifies a time-out as a floating point number in seconds.
# When the timeout argument is
