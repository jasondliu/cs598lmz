import select
# Test select.select()

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair(socket.AF_INET, socket.SOCK_STREAM)

# Make them non-blocking
sock1.setblocking(False)
sock2.setblocking(False)

# Send data from sock1 to sock2
sock1.send(b'x')

# Wait for data to become available
ready = select.select([sock2], [], [])
if ready[0]:
    data = sock2.recv(100)
    print('Received', repr(data))
else:
    print('Timed out')

# Send data from sock2 to sock1
sock2.send(b'y')

# Wait for data to become available
ready = select.select([sock1], [], [])
if ready[0]:
    data = sock1.recv(100)
   
