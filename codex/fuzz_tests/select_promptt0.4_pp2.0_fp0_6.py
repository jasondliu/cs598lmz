import select
# Test select.select()

# Create a pair of connected sockets

(server, client) = socket.socketpair()

# Make them non-blocking

server.setblocking(0)
client.setblocking(0)

# Fill the server socket's send buffer

server.send(b"x" * (65536 * 2))

# Check that the client socket is readable but not writable

print("Before select:")

readable, writable, exceptional = select.select([client], [], [])

print("Readable:", readable)
print("Writable:", writable)
print("Exceptional:", exceptional)

# Empty the server socket's send buffer

while True:
    try:
        data = server.recv(65536)
        if not data:
            break
    except BlockingIOError:
        pass

# Check that the client socket is now writable but not readable

print("\nAfter select:")

readable, writable, exceptional = select.select([], [client], [])

print("Readable:", readable)
print("Writable
