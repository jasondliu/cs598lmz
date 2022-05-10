import selectors
import socket
import sys
import types

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

# Create a selector
sel = selectors.DefaultSelector()

# Register the socket to be monitored for data arrival
sel.register(sock, selectors.EVENT_READ, data=None)

# Create a list of messages to send
messages = [b'Message 1 from client.', b'Message 2 from client.']

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            print('received
