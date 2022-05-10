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

client_socket.sendall(b"Hello from client")

# Wait for the data to arrive from the client

ready = select.select([server_socket], [], [], 5)

if ready[0]:
    data = server_socket.recv(1024)
    print("Received:", data)
else:
    print("Timed out")

# Send some data from the server to the client

server_socket.sendall(b"Hello from server")

# Wait for the data to arrive from the server

ready = select.select([client_socket], [], [], 5)

