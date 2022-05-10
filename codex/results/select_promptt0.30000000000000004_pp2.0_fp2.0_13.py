import select
# Test select.select()
import socket

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# Send some data from sock1
sock1.send(b'x')

# Wait for data to become available on sock1
print('Waiting for data...')
readable, writable, exceptional = select.select([sock1], [], [])

# Sockets are ready to be read
print('Ready:', readable)

# Receive the data
print('Received:', sock1.recv(1024))
