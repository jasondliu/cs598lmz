import select
# Test select.select()

# Create a pair of connected sockets

# To test select.select() with sockets, we need to create a pair of connected sockets.
# We do this by creating a pair of sockets, binding them to a pair of ports, and then
# connecting them together.

import socket
import sys
import time

# Create a pair of connected sockets

def create_sockets(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', port))
    server.listen(1)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', port))
    return server, client

# Run a simple test: send a byte to the server and read it back

def test_simple_echo(port):
    server, client = create_sockets(port)
    connection, address = server.accept()
    client.send(b'1')
    one = connection.recv(1)
    assert one == b'1'

