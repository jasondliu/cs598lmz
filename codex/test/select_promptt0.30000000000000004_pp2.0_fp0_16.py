import select
# Test select.select

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until a monitored file descriptor becomes ready; if zero, do not block at all; otherwise, block for at most timeout seconds

# return value: three lists of objects that are ready

# select.error: exception raised on select.select() error

# select.poll()
# select.poll() is a cross-platform version of select() that works on many Unix platforms as well as Windows.

# select.poll() returns a poll object, which supports registering and unregistering file descriptors, and then polling them for I/O events.

# select.poll() is available on Unix and Windows.

# select.poll() is a more low-level interface than select().

# select.poll() supports a wider range of file descriptors than select().

# select.poll() is slower than
