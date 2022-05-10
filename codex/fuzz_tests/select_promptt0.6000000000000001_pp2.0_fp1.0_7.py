import select
# Test select.select()
rlist = []
wlist = []
xlist = []

# The select.select() function takes three lists of file descriptors.
# The first contains file descriptors that you want to monitor for
# being ready to read from. The second contains file descriptors
# that you want to monitor for being ready to write to. The third
# contains file descriptors that you want to monitor for errors.

# The function will return a tuple of three lists. Each list will
# contain the file descriptors that are ready for the corresponding
# I/O operation.

# If the timeout argument is specified and not None, then it should
# be a float specifying a timeout for the operation in seconds.
# If the timeout expires before any of the specified file descriptors
# are ready, then select will return three empty lists.

# If the timeout argument is omitted, or is None, then select will
# block until some of the specified file descriptors are ready.

# If all lists are empty, then select() will block forever.

print "select.select(rlist, wlist, xlist, timeout)"
print "rlist
