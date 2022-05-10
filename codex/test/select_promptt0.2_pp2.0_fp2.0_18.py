import select
# Test select.select()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Make them non-blocking

sock1.setblocking(0)
sock2.setblocking(0)

# Fill the sockets with some data

sock1.send(b'x' * 1000000)
sock2.send(b'y' * 1000000)

# Check that the sockets are readable

print('Before: ', select.select([sock1], [], []))
print('After: ', select.select([sock1], [], []))

# Empty the sockets

sock1.recv(100)
sock2.recv(100)

# Check that the sockets are readable again

print('After: ', select.select([sock1], [], []))

# Close the sockets

sock1.close()
sock2.close()

# Check that the sockets are readable one last time

