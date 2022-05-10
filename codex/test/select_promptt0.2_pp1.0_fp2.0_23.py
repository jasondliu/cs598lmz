import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if negative, block indefinitely

# Return value: three lists of objects that are ready: subsets of the first three arguments

# select.select() is a useful way to multiplex input and output, for example, when you have a user interface with a “Submit” button and you want to wait for either a click on the button or some input in an Entry.

# The following example uses select() to wait for a button click or a keypress, but it will miss mouse movements, and it will not process any other events while it is waiting.

# The following example uses select() to wait for a button click or a keypress, but it will miss mouse movements, and it will not process any other events while it is waiting.
