import select
# Test select.select()

# This is a simple test program that will create two sockets,
# register them with select, and then monitor them for input.
# The program will exit when either socket has input.

# Create two sockets.
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind them to something.
s1.bind(('', 0))
s2.bind(('', 0))

# Get the port numbers.
p1 = s1.getsockname()[1]
p2 = s2.getsockname()[1]

# Register them with select.
r, w, e = select.select([s1], [], [])
r, w, e = select.select([s2], [], [])

# Create a client.
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server.
c.connect(('localhost', p1))

# Wait
