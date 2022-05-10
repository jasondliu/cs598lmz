import select
# Test select.select()

# List of sockets to be monitored
inputs = [ ]

# Sockets from which we expect to read
inputs.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

# Sockets from which we expect to write
outputs = [ ]

# Outgoing message queues (socket:Queue)
message_queues = {}

# Set up the socket
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

# Add the server socket to the list of readable connections
inputs.append(sock)

while inputs:

    # Wait for at least one of the sockets to be ready for processing
    print >>sys.stderr, '\nwaiting for the next event'
    readable, writable, exceptional = select
