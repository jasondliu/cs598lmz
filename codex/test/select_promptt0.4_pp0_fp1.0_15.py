import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# Example:
r, w, x = select.select([sys.stdin], [], [], 1)

if r:
    print("Got input from stdin:", sys.stdin.readline().rstrip())
else:
    print("No input from stdin")

# select.select() can also be used with sockets.
# select.select() is a low-level API.
# The high-level API is provided by the socket module.
# select.select() is not supported on all platforms.
# select.select() is not supported on Windows.
# select.select() is not supported on Mac OS X.
# select.select() is not supported on Linux with a threading model other than 1:1.
