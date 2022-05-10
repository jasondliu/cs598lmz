import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
#     rlist: wait until ready for reading
#     wlist: wait until ready for writing
#     xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
#     timeout: if not specified, will block until a monitored file descriptor becomes ready
#
# Return value: three lists of objects that are ready
#
# Example:
#
# >>> select.select([sys.stdin], [], [], 0.0)[0]
# [<open file '<stdin>', mode 'r' at 0xb7e348f0L>]
# >>> select.select([sys.stdin], [], [], 1.0)[0]
# []
# >>>
#
# From: http://www.doughellmann.com/PyMOTW/select/
