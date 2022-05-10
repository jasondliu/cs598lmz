import select
# Test select.select()

# Create a pair of connected sockets
socks = [socket.socketpair()]

# Add a few more sockets
for x in range(3):
    socks.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

for s in socks:
    s.setblocking(0)

# Create a pair of connected sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 0))
server_socket.listen(1)

# Connect the first socket to server_socket
socks[0].connect(server_socket.getsockname())

# Accept the connection with server_socket and send data
connection, address = server_socket.accept()
connection.send(b'xyz')

# Connect the second socket to server_socket
socks[1].connect(server_socket.getsockname())

# Create readers and writers lists
readers = [socks[0], connection]
writers = [socks[1]]

# Create an
