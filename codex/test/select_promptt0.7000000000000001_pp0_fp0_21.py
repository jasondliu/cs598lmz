import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
#
#    rlist -- wait until ready for reading
#    wlist -- wait until ready for writing
#    xlist -- wait for an ``exceptional condition'' (see the manual page)
#
# If only one kind of condition is required, pass [] for the other lists.
#
# A ready socket object has one or more of these conditions true:
#
#    select.POLLIN
#        there is data to be read (includes OOB data if POLLPRI is set)
#    select.POLLPRI
#        there is urgent data to read
#    select.POLLOUT
#        writing now will not block
#    select.POLLERR
#        an error occurred (only if POLLHUP is not set)
#    select.POLLHUP
#        the connection has been shutdown (only if POLLIN and POLLOUT
#        are both clear)
#    select.POLLNVAL
#        invalid request: descriptor not open
#
# Return value: three lists of
