import select
# Test select.select()
# select.select() is a blocking call.
# It waits until any of the file descriptors is ready for some I/O operation.
# select.select() takes three lists:
#   - the first contains the file descriptors to be monitored for being able to read from (level-triggered)
#   - the second contains the file descriptors to be monitored for being able to write to (level-triggered)
#   - the third contains the file descriptors to be monitored for errors (level-triggered)
# select.select() returns three lists with the subset of the passed file descriptors:
#   - the first contains the subset of the file descriptors that are ready for reading
#   - the second contains the subset of the file descriptors that are ready for writing
#   - the third contains the subset of the file descriptors that have an error condition
# select.select() can be interrupted by a signal (e.g., SIGINT)
# select.select() can be interrupted by a signal handler that calls signal.alarm()
# select.select() can be interrupted by a signal handler that calls signal.setitimer
