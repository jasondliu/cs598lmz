import select
# Test select.select()

# Create a pair of connected sockets
server, client = socket.socketpair()

# Make one non-blocking
client.setblocking(0)

# Some data to send
data = b"ABC"

# Try a few times to send the data
for i in range(5):
    try:
        sent = client.send(data)
        break
    except BlockingIOError:
        pass

# Check what was sent
print("Sent:", sent)

# Wait for the data to be received
inputs = [server]
outputs = []
timeout = 1

readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)

# Check what was received
print("Read:", server.recv(1024))

# Clean up
for s in [server, client]:
    s.close()

# Test select.poll()

# Create a pair of connected sockets
server, client = socket.socketpair()

# Make one non-blocking
client.setblocking(0)

# Some data to send
