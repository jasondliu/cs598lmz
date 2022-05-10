import select
# Test select.select()
#
#   select.select(rlist, wlist, xlist[, timeout])
#
#   rlist: wait until ready for reading
#   wlist: wait until ready for writing
#   xlist: wait for an "exceptional condition" (see the manual page for what
#          your system considers such a condition)
#
#   timeout: how long to wait for an event.
#            None: wait forever
#            0.0: don't wait at all
#            >0.0: wait up to that many seconds
#
#   The return value is a tuple of three lists corresponding to the
#   first three arguments; each contains the subset of the corresponding
#   file descriptors that are ready.
#
#   A file descriptor is either a socket or file object, or a small integer
#   gotten from a fileno() method call on one of those.
#
#   *** IMPORTANT NOTE ***
#
#   The lists returned by select() are *not* guaranteed to be in any
#   particular order, and may be arbitrarily re-ordered by the underlying
#   system. 
