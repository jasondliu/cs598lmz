import select
# Test select.select
# Use: http://docs.python.org/2/library/select.html

# We will use select to create a server that responds to requests
# See: http://docs.python.org/2/howto/sockets.html

# STILL TO DO
# - Test to make sure that FDs are correct
#   (ie. Check that ret[0] == ret[1] == [])
# - Add timeout to select.select
# - Adding a client should push everything else back
#   (ie. ret[2] should contain the previous clients)

import socket
import select

HOST = '127.0.0.1'
PORT = 65432

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_sock.bind((HOST, PORT))
listen_sock.listen(5)

client_sockets = []

# Set up stdin as non-blocking
# This will allow us to check stdin as well as the clients
# See: http://docs.python.
