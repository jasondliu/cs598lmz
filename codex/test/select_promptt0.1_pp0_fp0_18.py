import select
# Test select.select()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Pass them to select()

r, w, e = select.select([sock1], [], [])

# Sockets are ready for reading
