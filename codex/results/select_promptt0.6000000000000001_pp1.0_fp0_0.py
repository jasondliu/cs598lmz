import select
# Test select.select()
# Select can be used to wait for the readyness of one or more file descriptors.
# It can also be used to wait for a timeout or until a signal arrives.
#
# select() returns three lists of file descriptors.
# The first list contains file descriptors that are ready for reading.
# The second list contains file descriptors that are ready for writing.
# The third list contains file descriptors that have an exception condition pending.
#
# If all three lists are empty, then select() timed out.
# The timeout argument specifies the time in seconds to wait.
# The value 0 indicates that select() should return immediately.
# The value None indicates that select() should wait indefinitely.
#
# select() takes three parameters.
# The first is a list of file descriptors to be checked for readiness to read.
# The second is a list of file descriptors to be checked for readiness to write.
# The third is a list of file descriptors to be checked for an exceptional condition.
#
# select() returns three lists of file descriptors.
# The first list contains file descriptors that are ready for reading.
# The second
