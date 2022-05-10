import select
# Test select.select()
# Note : use select.select(rlist,wlist,elist,[timeout])
# rlist,wlist,elist : all three parameters are list, every element in the list is a file descriptor
# they are used to indicate which file descriptor you're interested in knowing about, in the case of an error
# or if the file descriptors you've indicated can be read from or written to.

# select function returns 3 lists, respectively for the file descriptors that are readable, writeable,
# and have an error condition.

# If you've indicated a timeout in your call to select(), the call will block until either data is
# available, or until your time is expired. If you've indicated a timeout of 0, the call will return
# immediately with the current status of the file descriptors, without blocking.

# You can use the select function to monitor multiple file descriptors at the same time, which you
# might want to do if you're reading data from a number of files, or network streams.

# if you want to get the current available data, you can make a call to select.select([fd],[],[],0)
# this
