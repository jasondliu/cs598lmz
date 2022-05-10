import select
# Test select.select

# Create a socket
s = socket.socket()

# Set the socket to non-blocking
s.setblocking(0)

# Connect to the socket
s.connect(("www.sina.com.cn", 80))

# Create a file-like object to read from
f = s.makefile()

# Read a line from the file-like object
print f.readline()
