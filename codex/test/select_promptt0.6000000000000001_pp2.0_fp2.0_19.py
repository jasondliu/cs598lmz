import select
# Test select.select()
# The select.select() function is a straightforward way to watch for I/O events
# on multiple file descriptors. It works on Windows and most Unix-like systems.

# The first argument to select() is a list of file descriptors to be watched for
# input events (reads). The second argument is the list of file descriptors to be
# watched for output events (writes). The third is a list of file descriptors to
# be watched for errors. The select() function monitors all the file descriptors
# passed and returns three lists of file descriptors: those that are ready for
# reading, those ready for writing, and those with errors.

# The select() function supports a fourth argument, which is the timeout. This
# is a floating-point number of seconds to wait for the events. If the timeout
# is omitted, select() blocks until at least one file descriptor is ready. If
# the timeout is zero, select() does not block, but returns the current status
# of the monitored file descriptors.

# For example, the following code sets up two sockets for listening for
# connections and then uses select() to monitor both
