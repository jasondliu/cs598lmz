import select
# Test select.select() to monitor a socket for incomming data.
#
# The select.select() method take three lists, the first two
# being the sockets to monitor for incomming or outgoing data
# (first list is for reading and the second is for writing).
#
# The third list is optional and contains sockets on wich an
# exception occured and should be monitored.
#
# The select.select() method returns three lists (or None in
# case of error) containing, the first one the sockets whith
# incomming data, the second the sockets for which we can send
# data and the third those with errors occured.
#
# The problem is that, when the socket is in non-blocking mode,
# the select.select() method will not wait for the socket to be
# ready and will immediately return with empty lists.  Below
# there is a little code to try to workaround this problem.
# Indeed, it seems that setting the socket to block just before
# the call to select.select() is enough.
#
# The problem is that, in some cases, the socket is not found
# in the lists returned
