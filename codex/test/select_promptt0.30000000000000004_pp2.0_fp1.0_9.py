import select
# Test select.select()

# Create a pair of connected sockets

server_socket, client_socket = socket.socketpair()

# Create a pair of connected sockets

server_socket, client_socket = socket.socketpair()

# Make them non-blocking

server_socket.setblocking(0)
client_socket.setblocking(0)

# Send some data from the client

client_socket.send(b'x')

# Wait for the data to arrive

ready = select.select([server_socket], [], [])

if ready[0]:
    data = server_socket.recv(1024)
    print('got:', data)
else:
    print('timed out')

# Send some data from the client

client_socket.send(b'x')

# Wait for the data to arrive

ready = select.select([server_socket], [], [])

if ready[0]:
    data = server_socket.recv(1024)
