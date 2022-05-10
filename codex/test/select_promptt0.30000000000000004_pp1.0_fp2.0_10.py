import select
# Test select.select()

#
# Create a pair of connected sockets
#

server_socket, client_socket = socket.socketpair()

#
# Make both sockets non-blocking
#

server_socket.setblocking(False)
client_socket.setblocking(False)

#
# Send some data from the client to the server
#

client_socket.send(b"This is the message.  There are many like it, but this one is mine.")

#
# Read the data from the server
#

data = server_socket.recv(1024)

print("Read %d bytes from the server" % len(data))

#
# Now, create a second pair of connected sockets
#

server_socket2, client_socket2 = socket.socketpair()

#
# Make both sockets non-blocking
#

server_socket2.setblocking(False)
client_socket2.setblocking(False)

#
# Send some data from the client to the server
