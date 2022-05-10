import select
# Test select.select()

#
#  select.select(rlist, wlist, xlist[, timeout])
#
#  rlist: wait until ready for reading
#  wlist: wait until ready for writing
#  xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
#
#  The return value is a triple of lists of objects that are ready:
#    sublists corresponding to the sequences of wait objects
#
#  The optional timeout argument specifies a time-out as a floating point number in seconds.
#    When the timeout argument is omitted the function blocks until at least one file descriptor is ready.
#    A time-out value of zero specifies a poll and never blocks.
#
#  The select() function monitors all sockets and pipes registered in rlist, wlist and xlist
#    until one or more of the following conditions are met:
#    1. A socket or pipe is ready for reading or writing.
#    2. A socket or pipe has an error condition pending.
#    3. A socket or pipe has an out-of-band data pending
