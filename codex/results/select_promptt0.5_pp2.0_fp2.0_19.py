import select
# Test select.select()

print('Starting')

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

# Create a file-like object for the socket
fileobj = sock.makefile('r')

# Wait for data
readable, writable, exceptional = select.select([fileobj], [], [], 5)

# Print the list of sockets that are ready to be read
print('readable:', readable)

# Print the list of sockets that are ready to be written to
print('writable:', writable)

# Print the list of sockets that have raised exceptions
print('exceptional:', exceptional)

# Receive data
data = fileobj.readline()
print('received "%s"' % data)

# Close the socket
sock.close()
</code>
And this is the server
