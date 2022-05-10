import select
# Test select.select()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Create a pair of connected sockets

sock1, sock2 = socket.socketpair()

# Make them non-blocking

sock1.setblocking(0)
sock2.setblocking(0)

# Fill up sock1's send buffer

for i in range(10):
    sock1.send(b'x' * 1000)

# Peek at the data without removing it from the buffer

print(sock1.recv(1000, socket.MSG_PEEK))

# Wait for data to become available

print('Waiting for data')

readable, writable, exceptional = select.select([sock1], [], [])

print('sock1 is readable:', readable)

# Now drain the buffer

while True:
    try:
        data = sock1.recv(1000)
    except BlockingIOError:
        break
    else:
        print('Received', len(data), 'bytes')


