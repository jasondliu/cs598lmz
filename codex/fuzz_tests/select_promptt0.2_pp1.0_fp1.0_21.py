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
msg = b"x" * 1000000

while True:
    try:
        sent = sock1.send(msg)
        break
    except BlockingIOError:
        pass

print("buffer full")

# Wait until the socket is readable
readable, writable, exceptional = select.select([sock2], [], [])

print("readable:", readable)

# Read the data
print(sock2.recv(100))

# We are done, close the socket
sock1.close()
sock2.close()
