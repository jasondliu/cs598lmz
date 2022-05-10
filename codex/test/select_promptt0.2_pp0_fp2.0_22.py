import select
# Test select.select()

# Create a pair of connected sockets

server, client = socket.socketpair()

# Make each non-blocking

server.setblocking(0)
client.setblocking(0)

# Feed data to client

client.send(b'x')

# Run select() to wait for input

print('Waiting for ready...')
readable, writeable, exceptional = select.select([server], [], [])

# When data is available, recv() won't block

print('Ready:', readable)
print('         Receiving from server:', server.recv(100))

# Close sockets

server.close()
