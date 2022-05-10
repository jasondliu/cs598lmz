import select
# Test select.select()

# Create a pair of connected sockets

import socket

sock1, sock2 = socket.socketpair()

# Make them non-blocking

sock1.setblocking(0)
sock2.setblocking(0)

# Send a message from one end

sock1.send(b"Hello from one")

# Read the message on the other end

select.select([sock2], [], [])

print(sock2.recv(100))

# Send a message from the other end

sock2.send(b"Hello from the other")

# Read the message on the other end

select.select([sock1], [], [])

print(sock1.recv(100))

# Close the sockets

sock1.close()
sock2.close()

# Test select.poll()

# Create a pair of connected sockets

import socket

sock1, sock2 = socket.socketpair()

# Make them non-blocking

sock1.setblocking(0)

