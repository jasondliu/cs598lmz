import select
# Test select.select
# select.select(rlist, wlist, xlist[, timeout])
#   rlist: wait until ready for reading
#   wlist: wait until ready for writing
#   xlist: wait for an "exceptional condition" (see the manual page for what your system considers such a condition)
#   timeout: if not given, will block until a monitored file descriptor becomes ready; if zero, will never block and return three empty lists; if a positive number, will block for at most that number of seconds
# Returns three lists of file descriptors: those that are ready for reading, those ready for writing, and those that have raised exceptions
# Note: if the time out is reached before anything interesting happens, select() returns three empty lists
# Note: select() does not necessarily return in any particular order, so if you are polling more than one file descriptor, you need to organize the results yourself
# Note: select() is a system call and therefore in the "slow" path
# Note: select() modifies the lists it receives as arguments, so you cannot use them for anything else while you are waiting
# Note: if you are using select() to multiplex input from
