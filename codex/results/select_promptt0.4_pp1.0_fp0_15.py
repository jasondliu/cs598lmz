import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition).
# timeout: wait until a timeout occurs
#
# The return value is a triple of lists of objects that are ready:
# (subset of rlist, subset of wlist, subset of xlist)
#
# If the time limit is reached with no file descriptors ready, three empty lists are returned.
#
# If the time limit is None, the call will never time out.
#
# select.select() can be interrupted by a signal (see the signal module).
#
# select.select() can also be used with pipes:
#
# >>> r, w, x = select.select([pipe_r], [], [])
# >>> if r:
# ...     data = os.read(pipe_r, 1000)
#
# In this example, if data is available on the pipe,
