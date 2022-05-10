import select
# Test select.select

# Create a pair of connected sockets

import socket
import select

sock1, sock2 = socket.socketpair()

# Make them non-blocking

sock1.setblocking(0)
sock2.setblocking(0)

# Send some data

for i in range(10):
    sock1.send(b"A")
    sock2.send(b"B")

# Read some data

for i in range(10):
    print(sock2.recv(1))
    print(sock1.recv(1))

# Now use select to wait until one or the other is ready to read

print("Waiting for ready...")

readable, writable, exceptional = select.select([sock1, sock2], [], [])

print("Ready:", readable, writable, exceptional)

# Read the data

print(readable[0].recv(1))
