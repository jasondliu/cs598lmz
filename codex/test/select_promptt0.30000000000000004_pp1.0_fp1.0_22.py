import select
# Test select.select()

# select.select() takes three arguments:
#  1. a list of file descriptors to monitor for input
#  2. a list of file descriptors to monitor for output
#  3. a list of file descriptors to monitor for error
#
# It returns three lists:
#  1. a list of file descriptors that are ready for input
#  2. a list of file descriptors that are ready for output
#  3. a list of file descriptors that are ready for error

# This example will monitor standard input (fd 0) for input,
# and will return immediately if there is input available.

# Create a pipe
r, w = os.pipe()

# Set the pipe to non-blocking
fcntl.fcntl(r, fcntl.F_SETFL, os.O_NONBLOCK)

# Create a list of file descriptors to monitor for input
inputs = [0, r]

# Create empty lists for output and error
