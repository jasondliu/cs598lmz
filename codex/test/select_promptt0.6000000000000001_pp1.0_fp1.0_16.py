import select
# Test select.select
# A simple echo server

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
sock.bind(server_address)
sock.listen(1)

# Wait for a connection
print('waiting for a connection')
connection, client_address = sock.accept()

