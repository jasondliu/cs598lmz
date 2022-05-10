import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
# timeout: if not specified, block until a monitored file descriptor becomes ready

# Return value: three lists of objects that are ready: subsets of the first three arguments

# Example:
# >>> import select
# >>> select.select([], [], [], 5.0)
# ([], [], [])
# >>>

# The example above waits for 5 seconds, and since no file descriptors were passed as arguments, it returns three empty lists.

# Task

# You are given a function .
# You are also given  lists. The  list consists of  elements.
# You have to pick one element from each list so that the value from the equation below is maximized: 

# %

# denotes the element picked from the  list . Find the maximized value  obtained.

# denotes the modulo operator.
