import select
# Test select.select function
#

# This function returns a list of all the file descriptors that are ready for reading
# and writing.
#
# The first parameter is a list of file descriptors to check for reading.
#
# The second parameter is a list of file descriptors to check for writing.
#
# The third parameter is a list of file descriptors to check for error conditions.
#
# The fourth parameter is the maximum time to wait in seconds.  If it is zero, then
# the function will not wait at all and will return immediately.  If it is negative,
# then the function will wait until an event occurs.
#
# The return value is a tuple with three elements.  The first element is a list of
# file descriptors that are ready for reading.  The second element is a list of
# file descriptors that are ready for writing.  The third element is a list of
# file descriptors that have an error condition.
#
# Note that the file descriptors are returned in the order that they were passed in.
#
# For example, the following code will wait for one second for a file descriptor to
# become
