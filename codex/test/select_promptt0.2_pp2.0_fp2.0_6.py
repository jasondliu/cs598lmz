import select
# Test select.select()

# Create a pair of connected sockets

server, client = socket.socketpair()

# Make each non-blocking

server.setblocking(0)
client.setblocking(0)

# Feed data to client

client.send(b'x')

# Run select() on server socket

readable, writable, exceptional = select.select([server], [], [])

# Check if select reported the socket as readable

print('READABLE:', readable)

# Receive a single byte of data from server

data = server.recv(100)

# Check byte of data received

print('DATA:', data)
