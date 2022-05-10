import select
# Test select.select()

# We need to create a non-blocking socket to test select()
# This code is not for production use!

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Make the socket nonblocking
sock.setblocking(0)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

# Wait for a response
amount_received = 0
amount_expected = len('Hello, world')

while amount_received < amount_expected:
    # Create a timeout (in seconds)
    timeout = 1

    # Create a list of sockets we wish to wait for a read event
    read_sockets, write_sockets, error_sockets = select.select([sock], [], [], timeout)

    if not read_sockets:
        print('No response from server. Resetting connection.')
        sock = socket.socket(socket
