import select
# Test select.select()

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# Send a message from sock1 to sock2
sock1.send(b'\x01\x02\x03\x04')

# Read the message from sock2
data = sock2.recv(1024)

# Check that the message was received
assert data == b'\x01\x02\x03\x04'

# Close the sockets
sock1.close()
sock2.close()

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# Send a message from sock1 to sock2
sock1.send(b'\x01\x02\x03\x04')

# Read the message from sock2
data = sock2.recv(1024)

# Check that the message was received
assert data == b'\x01\x02\x03\x04'

# Close the sockets
sock1.close()
sock2.close()

# Create a pair
