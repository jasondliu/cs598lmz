import select
# Test select.select()

# Create two sockets, one for listening and one for sending
sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sending_socket.bind(('localhost', 0))
listening_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
listening_socket.bind(('localhost', 0))

# Create a message to send
message = 'Hello, world!'

# Send the message
sending_socket.sendto(message, listening_socket.getsockname())

# Wait for the message to arrive
readable, writable, exceptional = select.select([listening_socket], [], [], 5)

# Check that the message has arrived
if listening_socket in readable:
    data, address = listening_socket.recvfrom(1024)
    print 'Received %r from %r' % (data, address)
else:
    print 'No data received'
</code>

