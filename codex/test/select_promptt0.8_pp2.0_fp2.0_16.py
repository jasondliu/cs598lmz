import select
# Test select.select()

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5001))
server_socket.listen(5)

# Accept connections from outside
(client_socket, address) = server_socket.accept()

# Now do something with the client_socket
# In this case, we'll pretend this is a threaded server
