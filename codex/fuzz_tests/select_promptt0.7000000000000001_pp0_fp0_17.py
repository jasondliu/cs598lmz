import select
# Test select.select function

# First argument is a list of file descriptors to monitor
# Second argument is a list of file descriptors to monitor for being writable
# Third argument is a list of file descriptors to monitor for exceptions
# Fourth argument is a time value to wait until returning

# It returns three lists, one of file descriptors that are ready to be read,
# one of file descriptors ready to be written to, and one of file descriptors
# with an exception

# select.select returns immediately if the time value is 0, then it does not
# wait for anything

# To monitor for a network connection, use a socket object
# To monitor for a file to be available for reading, use an open file object

# To monitor for a file to be writable,
# open the file in write mode and call fileno() on it

# To monitor for a file to have an exception, use an open file object

# If the file object is a tty device, you can monitor for an exception when
# a key is pressed or a line is available for reading

inputs = [open('/tmp/x')]
outputs
