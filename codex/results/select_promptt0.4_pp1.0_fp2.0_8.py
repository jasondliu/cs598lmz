import select
# Test select.select()

# Create a pair of connected sockets

(server_socket, client_socket) = socket.socketpair()

# Make them non-blocking

server_socket.setblocking(0)
client_socket.setblocking(0)

# Fill the server socket with some data

server_socket.send(b"Hello from server")

# Peek at the data

print("Before select:")
print(repr(client_socket.recv(1024, socket.MSG_PEEK)))

# Wait for the client socket to be readable

print("Waiting for the client socket to be readable")
readable, writable, exceptional = select.select([client_socket], [], [])

print("After select:")
print(repr(client_socket.recv(1024, socket.MSG_PEEK)))

# The data is still there, because the client socket is in non-blocking
# mode. If we now do a normal recv() call, we'll get the data

print("Doing a normal recv() call:")
print(repr(client_
