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

client_socket.send("This is the message.  There are many like it, but this one is mine.")

# Wait for the data to arrive

while True:
    readable, writable, exceptional = select.select([server_socket], [], [])
    if server_socket in readable:
        break

# Read the data from the server
