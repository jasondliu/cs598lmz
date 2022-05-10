import select
# Test select.select()

# Create a pair of connected sockets

server_socket, client_socket = socket.socketpair()

# Create a pair of connected sockets

server_socket, client_socket = socket.socketpair()

# Make them non-blocking

server_socket.setblocking(False)
client_socket.setblocking(False)

# Fill the server socket with data

server_socket.send(b"x" * 4096)

# Peek at the data

print("Before select:")
print("readable:", select.select([server_socket], [], [], 0))
print("writable:", select.select([], [client_socket], [], 0))
print("errors:", select.select([], [], [client_socket], 0))

# Consume the data

data = server_socket.recv(4096)
print("After select:")
print("readable:", select.select([server_socket], [], [], 0))
print("writable:", select.select([], [client_socket], [], 0))
print("errors:", select
