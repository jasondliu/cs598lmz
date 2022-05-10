import select
# Test select.select
# select.select(read_list, write_list, error_list, timeout)
# read_list, write_list, error_list are lists of sockets
# timeout is a float, in seconds
# returns read_list, write_list, error_list
# read_list, write_list, error_list have been modified to
# only contain sockets that are ready for the specified
# operation
#
# select.select(read_list, write_list, error_list, timeout)
# read_list, write_list, error_list are lists of sockets
# timeout is a float, in seconds
# returns read_list, write_list, error_list
# read_list, write_list, error_list have been modified to
# only contain sockets that are ready for the specified
# operation
#
# Note that select.select() is a blocking call, and will not
# return until the timeout period elapses, an error occurs,
# or one or more sockets are ready for the specified operation
#
# select.select() is also available as a method of socket objects
#
# select.select() can
