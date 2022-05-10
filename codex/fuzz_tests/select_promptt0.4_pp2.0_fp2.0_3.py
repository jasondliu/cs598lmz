import select
# Test select.select()

# select() takes 3 args:
#   1. a list of file descriptors to watch for input
#   2. a list of file descriptors to watch for output
#   3. a list of file descriptors to watch for exceptions

# select() returns a tuple of 3 lists:
#   1. a list of file descriptors that are ready for input
#   2. a list of file descriptors that are ready for output
#   3. a list of file descriptors that have exceptions

# select() is a blocking call

# select() is useful for multiplexing IO

# select() is a lower level call than poll()

# select() is limited by the number of file descriptors that can be watched
# (usually 1024)

# select() is supported on all platforms

# select() is not supported with sockets

# select() is not supported with pipes

# select() is not supported with ttys

# select() is not supported with regular files

# select() is not supported with devices

# select() is not supported with named pipes

# select() is not supported with directories
