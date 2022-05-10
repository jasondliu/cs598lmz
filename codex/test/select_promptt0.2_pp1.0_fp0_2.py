import select
# Test select.select()

# Create a pair of connected sockets

import socket

sock1, sock2 = socket.socketpair()

# Create a pair of connected sockets

import socket

sock1, sock2 = socket.socketpair()

# Pass them to select()

for s in select.select([sock1], [], [], 0)[0]:
    print(s.recv(100))

# Send data from sock2

sock2.send(b'Hello from sock2')

# Pass them to select()

for s in select.select([sock1], [], [], 0)[0]:
    print(s.recv(100))

# Send data from sock2

sock2.send(b'Hello from sock2')

# Pass them to select()

for s in select.select([sock1], [], [], 0)[0]:
    print(s.recv(100))

# Send data from sock2

sock2.send(b'Hello from sock2')

# Pass them to select()

