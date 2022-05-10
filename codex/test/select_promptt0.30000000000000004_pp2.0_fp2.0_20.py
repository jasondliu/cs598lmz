import select
# Test select.select()

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# Create a pair of connected sockets
sock1, sock2 = socket.socketpair()

# Make them non-blocking
sock1.setblocking(0)
sock2.setblocking(0)

# Send some data
sock1.send(b"123")
sock2.send(b"456")

# Set up the poller
poller = select.poll()
poller.register(sock1, select.POLLIN)
poller.register(sock2, select.POLLIN)

# Poll for data
for i in range(2):
    events = poller.poll(1000)
    print("events:", events)
    for fd, event in events:
        if fd == sock1.fileno():
            data = sock1.recv(100)
