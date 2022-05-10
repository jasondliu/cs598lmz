import select
# Test select.select
# Select() function is to monitor multiple sockets whether they are ready to perform I/O operations.
# select.select(rlist, wlist, xlist[, timeout])
# rlist: the sockets to be monitored for incoming data.
# wlist: the sockets to be monitored for availability to send data.
# xlist: the sockets to be monitored for exceptions.
# timeout: the maximum time to wait, in seconds.
# Return value is a tuple of three lists, containing the subsets of the first three arguments that are ready.
# If the timeout expires, three empty lists are returned
# If select() returns three empty lists, it means that the time limit has expired before anything interesting happened. 
# In other words, there was nothing to read, nothing to write, and no exceptions.
# If select() returns three non-empty lists, it means that there is something to read, something to write, or an exception pending. 
# Now you have to find out exactly what’s ready by calling recv(), send(), or some other method on each socket that’s ready.
# Example:
# if rlist:
#   for s
