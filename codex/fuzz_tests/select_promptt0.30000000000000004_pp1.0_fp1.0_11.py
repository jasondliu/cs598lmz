import select
# Test select.select()

# select.select() takes three arguments:
# 1. a list of file descriptors to monitor for reading
# 2. a list of file descriptors to monitor for writing
# 3. a list of file descriptors to monitor for errors
# It returns three lists of file descriptors:
# 1. file descriptors that are ready for reading
# 2. file descriptors that are ready for writing
# 3. file descriptors that have errors
#
# select.select() is a blocking call, meaning that it will wait until
# at least one of the file descriptors is ready for reading, writing,
# or has an error.

# This example uses select.select() to monitor a socket for reading
# and a pipe for writing.

# Create a pipe
r, w = os.pipe()

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.google.com', 80))

# Create a select.select() object
sel = select.select([s, r], [w], [])

# sel.
