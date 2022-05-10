import select
# Test select.select()

# select.select() takes three lists of file descriptors and waits until they are ready for reading, writing, or have an exceptional condition.
# It returns a tuple of three lists containing the subset of the file descriptors that are ready.
# select.select() can be used with sockets.

# Create a socket
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to a server
s.connect(("www.python.org", 80))

# Set the socket to non-blocking mode
s.setblocking(0)

# Send data
# The socket is non-blocking, so the call will return immediately.
# If the socket is not ready to send data, the call will fail with an error.
try:
    s.send(b"GET / HTTP/1.0\r\nHost: www.python.org\r\n\r\n")
except BlockingIOError:
    pass

# Wait for the response
# The socket is non-blocking, so the call will return immediately.
# If the socket is
