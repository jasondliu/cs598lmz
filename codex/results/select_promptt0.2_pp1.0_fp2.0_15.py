import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)

# Return value: three lists of objects that are ready

# select() can be told to wait for a limited time by passing a float value as the optional fourth argument.
# If the timeout period expires before any of the requested events occur, three empty lists are returned.

# select() can also be used with pipes, sockets, and other devices.

# select() is available on Unix and Windows.

# select() is a useful system call, but it’s not always easy to use.
# The selectors module provides a higher-level interface that is easier to use.
# The module is available on Unix, Windows, and Mac OS X.

# selectors.DefaultSelector()
# selectors.DefaultSelector.register(fileobj, events, data=None)
# selectors.DefaultSelector.unregister
