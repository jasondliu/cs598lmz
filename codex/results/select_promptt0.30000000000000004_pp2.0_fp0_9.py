import select
# Test select.select()

# select() takes 3 lists of file descriptors to watch
# 1st list: wait until ready for reading
# 2nd list: wait until ready for writing
# 3rd list: wait for errors
# Returns 3 lists of file descriptors that are ready

# select() is a blocking call, meaning that it will wait until
# at least one file descriptor is ready

# select() has a timeout argument, which is the max time to wait
# for a file descriptor to be ready. If the timeout is reached,
# select() will return 3 empty lists

# select() also has a optional 4th argument, which is the signal
# set to check for interrupts

# select() can be interrupted by a signal, and in that case, it
# will return 3 empty lists

# select() can be used to multiplex many file descriptors

# select() is available on Unix, Windows, and some Mac OS versions
# select() is not available on standard Mac OS

# select() is not available on standard Python, but the select
# module provides it

# select() is not available on standard Python, but the select
# module
