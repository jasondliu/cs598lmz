import select
# Test select.select()

# Create a pair of connected sockets

server, client = socket.socketpair()

# Make each non-blocking

server.setblocking(0)
client.setblocking(0)

# Feed data to client

client.send(b"x" * 1024)

# Run select() to wait for input

print("Waiting for ready-to-read sockets...")

readable, writable, exceptional = select.select([server], [], [])

print("Ready-to-read:", readable)

