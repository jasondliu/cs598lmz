import select
# Test select.select()

# Create a pair of connected sockets

server_socket, client_socket = socket.socketpair()

# Make them non-blocking

server_socket.setblocking(0)
client_socket.setblocking(0)

# Send some data

server_socket.send(b"x")

# Wait for it to arrive

readable, writable, exceptional = select.select([client_socket], [], [])

# The data is ready to be read

