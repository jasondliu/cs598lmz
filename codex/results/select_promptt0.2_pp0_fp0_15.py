import select
# Test select.select()

# Create a pair of connected sockets

server_socket, client_socket = socket.socketpair()

# Create a pair of connected sockets

server_socket, client_socket = socket.socketpair()

# Make them non-blocking

server_socket.setblocking(0)
client_socket.setblocking(0)

# Send some data from the client to the server

client_socket.sendall(b'x')

# Wait for the data to arrive

ready = select.select([server_socket], [], [])

# The ready list contains the server socket

print(ready[0])

# Receive the data

data = server_socket.recv(100)

# Check that the data matches

print(data)

# Send some data from the server to the client

server_socket.sendall(b'y')

# Wait for the data to arrive

ready = select.select([client_socket], [], [])

# The ready list contains the client socket

print(ready[0])

# Receive the data
