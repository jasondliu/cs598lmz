import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not specified, will block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready
# rlist: objects in rlist that are ready for reading
# wlist: objects in wlist that are ready for writing
# xlist: objects in xlist that have an “exceptional condition”

# select.select() will always return three lists, even if they are empty

# select.select() is a blocking call. If you want to make it non-blocking, you can pass a timeout value.
# If the timeout period value has passed, select() will return three empty lists.

# select.select() can be used to multiplex between many file descriptors,
# putting the current thread to sleep until one or more of the file descriptors
# become ready for some kind of
