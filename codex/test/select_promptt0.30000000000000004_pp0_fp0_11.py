import select
# Test select.select()

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# Make them non-blocking
sock1.setblocking(0)
sock2.setblocking(0)

# Fill up the buffer with some data
msg = bytes(range(0, 100))

while True:
    try:
        sent = sock1.send(msg)
        break
    except BlockingIOError:
        pass

print('sent:', sent)

# Read the data from the socket
while True:
    try:
        data = sock2.recv(1024)
        break
    except BlockingIOError:
        pass

print('received:', data)
