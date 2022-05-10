import select
# Test select.select() with a server socket

# Create two sockets, one for the server, one for the client
sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the sockets to localhost
sock_server.bind(('localhost', 0))
sock_client.bind(('localhost', 0))

# Get the port numbers
port_server = sock_server.getsockname()[1]
port_client = sock_client.getsockname()[1]

# Listen on the server socket
sock_server.listen(5)

# Connect the client to the server
sock_client.connect(('localhost', port_server))

# Accept the connection
sock_conn, addr = sock_server.accept()

# Set both sockets to non-blocking mode
sock_conn.setblocking(0)
sock_client.setblocking(0)

# Test select.select() with only the client socket and
