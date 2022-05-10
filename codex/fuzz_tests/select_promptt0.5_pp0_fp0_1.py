import select
# Test select.select()

# select.select(rlist, wlist, xlist[, timeout])
# 	Wait until one or more file descriptors are ready for some kind of I/O. 
# 	The first three arguments are sequences of file descriptors to be waited for: 
# 	rlist -- wait until ready for reading
# 	wlist -- wait until ready for writing
# 	xlist -- wait for an ``exceptional condition''
# 	If only one kind of condition is required, pass an empty list for the other arguments.
#	A file descriptor is ready if it is possible to perform the corresponding I/O operation (e.g., read()) without blocking the process.
#	select() may modify the lists it receives as arguments, and may also return a modified list of file descriptors.
#	The return value is a triple of lists of objects that are ready: subsets of the first three arguments. 
#	When the time-out is reached without a file descriptor becoming ready, three empty lists are returned.

#	Note: select() may not report a socket file descriptor as ready for reading until a subsequent call,
