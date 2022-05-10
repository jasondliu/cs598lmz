import select
# Test select.select()
# Note: select() should be passed three lists:
# (1) the first list contains all the objects to be checked for readability,
# (2) the second list contains all the objects to be checked for writability,
# and (3) the third list contains all the objects to be checked for errors.
# The return value of select() is actually a tuple of three lists.
# The first list in the tuple is a list of objects that are readable.
# The second list is a list of objects that are writable, and
# the third list is a list of objects that have raised exceptions.
# So a call to select() could look like this:
# readable, writable, exceptional = select.select(read_list, write_list, error_list, timeout)
# If the timeout period is over without any event, the three lists in the returned tuple will be empty.

# select() can also be used with sockets, and is the best method to use when dealing with sockets.
# select() can be used with sockets to check for new data arriving on the socket.
# The following code snippet reads from the socket only if there is data
