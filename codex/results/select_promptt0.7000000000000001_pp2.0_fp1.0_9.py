import select
# Test select.select()
#
# select.select(rlist, wlist, xlist[, timeout])
# 	Parameters:
# 		rlist -- wait until ready for reading
# 		wlist -- wait until ready for writing
# 		xlist -- wait for an “exceptional condition” (see the manual page for what your system considers such a condition)
# 		timeout -- wait until a timeout occurs
# 	Return value:
# 		Three lists corresponding to the first three arguments; each contains the subset of the corresponding file descriptors that are ready.
#
# 	Example: 
# 		import socket
# 		s = socket.socket()
# 		# create a socket ....
# 		select.select([s], [], [], 5.0) # wait for 5 seconds or until s is ready to read
#
# 	select() will block until one of the specified conditions is true. 
#	The return value is a triple of lists of objects that are ready: subsets of the first three arguments. 
#	When the time-out is
