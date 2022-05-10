import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
#
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until ready for reading, writing or exceptional condition

# Returns:
# Three lists of objects that are ready: subsets of the first three arguments.
# May raise OSError.

# Example:
# >>> select.select([sys.stdin], [], [], 0.0)[0]
# []
# >>> select.select([sys.stdin], [], [], 0.1)[0]
# [<open file '<stdin>', mode 'r' at 0x7f5a7d8c5ce0>]
# >>> select.select([sys.stdin], [], [], 0.0)[0]
# []
# >>> select.select([sys.stdin], [], [], 0.1)[0]
#
