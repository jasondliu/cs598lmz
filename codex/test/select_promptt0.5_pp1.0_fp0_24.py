import select
# Test select.select()
# select.select() is a blocking call, so it will not return until
# at least one of the file descriptors is ready for some kind of I/O
# select.select() takes three lists of file descriptors and will return
# subsets of those lists based on which file descriptors are ready for I/O
# select.select() can handle reading, writing and errors, so it will
# return three lists of file descriptors, one for each activity
# select.select() has a timeout, so you can specify how long to wait for
# I/O to be ready before giving up
# select.select() is available on Windows, Linux and Unix, so it's
# worth knowing about

# Create a non-blocking socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)

# Set up the socket parameters
server.bind(('localhost', 5001))
server.listen(5)

# Create a list of inputs
inputs = [server]

# Create a list of outputs
outputs = []

# Create a
