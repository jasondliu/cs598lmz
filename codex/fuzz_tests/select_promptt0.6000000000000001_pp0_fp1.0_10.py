import select
# Test select.select()
# Does it work with a socket?
# Does it work with a file?
# Does it work with a pipe?
# Does it work with a stdin?

# 1) Does it work with a socket?
# Yes, it does.
# The following returns a list with a single item (the socket)
# when data is available.
# It returns an empty list when there is no data.

import socket
import select

def make_server_socket(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', port))
    server_socket.listen(5)
    return server_socket

def make_client_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    return client_socket

# Set up
