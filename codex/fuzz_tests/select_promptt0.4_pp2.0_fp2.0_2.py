import select
# Test select.select()
# The first argument is a list of sockets to be checked for readability
# The second argument is a list of sockets to be checked for writability
# The third argument is a list of sockets to be checked for errors
# The return value is a tuple of three lists of sockets corresponding to the first three arguments

# The following example shows how to use select.select() to check for data available to read on a socket
# The example uses a timeout of 1 second
# If no data is available, the example prints a message and continues
# If data is available, the example prints the data and terminates

import socket
import sys
import select

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    # Send data
    message = b'This is the message.  It will be repeated.'
    print('sending
