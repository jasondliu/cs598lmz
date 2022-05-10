import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until ready

# Return value: three lists of objects that are ready

# Example:
# rlist, wlist, xlist = select.select([sys.stdin], [], [], 10)
# if rlist:
#     s = sys.stdin.readline()
#     print(s)
# else:
#     print('No input within 10 seconds.')

# Example:
# rlist, wlist, xlist = select.select([sys.stdin], [], [], 10)
# if rlist:
#     s = sys.stdin.readline()
#     print(s)
# else:
#     print('No input within 10 seconds.')

# Example:
# import socket
# s = socket.
