import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# timeout: if not given, block until at least one file descriptor is ready; if zero, return three empty lists; if a positive float, return three empty lists after that many seconds have elapsed; if negative float, block until at least one file descriptor is ready or the timeout has elapsed, whichever comes first

# return value: three lists of objects that are ready: subsets of the first three arguments

# example:
# rlist, wlist, xlist = select.select(rlist, wlist, xlist[, timeout])
# if rlist:
#     print('ready for reading:', rlist)
# if wlist:
#     print('ready for writing:', wlist)
# if xlist:
#     print('exceptional condition:', xlist)

# example:
# import select
# import
