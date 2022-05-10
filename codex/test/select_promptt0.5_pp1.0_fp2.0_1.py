import select
# Test select.select()
# select.select(rlist, wlist, xlist[, timeout])
# rlist: wait until ready for reading
# wlist: wait until ready for writing
# xlist: wait for an “exceptional condition” (not used here)
# timeout: if not supplied, block until a monitored file descriptor becomes ready

# Return three lists of objects that are ready: subsets of the first three arguments.
# A file descriptor is ready if it is possible to perform the corresponding I/O operation (e.g., read()) without blocking.

# Example:

# Create two sockets
sock1 = socket.socket()
sock2 = socket.socket()

# Make them non-blocking
sock1.setblocking(False)
sock2.setblocking(False)

# Connect them to a server (that isn't listening)
sock1.connect(("localhost", 8001))
sock2.connect(("localhost", 8002))

# Wait for them to be ready to read
