import select
# Test select.select()

# Create two sockets that are connected to each other.

sock1, sock2 = socket.socketpair()

# Make sock1 non-blocking.
sock1.setblocking(0)

# Make sock2 non-blocking.
sock2.setblocking(0)

# Make sock1 sendable.
sock1.send(b'x')

# Make sock2 receivable.
ret = select.select([sock2], [], [])
assert(ret == ([sock2], [], []))

# Make sock2 sendable.
sock2.send(b'x')

# Make sock1 receivable.
ret = select.select([sock1], [], [])
assert(ret == ([sock1], [], []))

# Make sock1 receivable.
ret = select.select([sock1], [], [])
assert(ret == ([], [], []))

# Make sock1 sendable.
sock1.send(b'x')

# Make sock2 receivable.
