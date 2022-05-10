import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return immediately even if no file descriptors are ready; if given and not zero, it specifies a timeout in seconds (float allowed) after which the select() call will return even if no file descriptors are ready

# Return value: three lists of file descriptors: rlist, wlist, xlist

# Example:
# >>> import select
# >>> r, w, x = select.select([sys.stdin], [], [], 10)
# >>> if r:
# ...     print sys.stdin.readline()
# ... else:
# ...     print 'Timed out'
# ...
# hello
# hello
# >>>

# select.poll()
# select.poll() is a cross-platform alternative to select
