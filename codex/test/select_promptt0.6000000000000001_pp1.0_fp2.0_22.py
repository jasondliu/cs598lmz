import select
# Test select.select()
# https://docs.python.org/3.4/library/select.html
# https://docs.python.org/3.4/library/socket.html#socket.socket.recv

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
# Server_address = ('localhost', 10000)
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address, file=sys.stderr)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection', file=sys.stderr)
