import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if given, block for at least that many seconds (can be a float, and timeouts are rounded to the system clock granularity, and may be longer than requested)

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select() can be used as an efficient way to multiplex input/output over a number of sockets.

# The following example shows how to use select() to multiplex two sockets and standard input.

# The example is written for UNIX; on Windows, replace "import select" with "import selectors" and change the line "sel.select(rlist, wlist, xlist)" to "events = sel.select(rlist, wlist, x
