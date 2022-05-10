import selectors
import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# Create a selector object
sel = selectors.DefaultSelector()

# Register the socket to monitor for read events
sel.register(sock, selectors.EVENT_READ, data=None)

# Send data
message = b'This is the message.  It will be repeated.'
print('sending {!r}'.format(message))
sock.sendall(message)

# Monitor the socket for read events
while True:
    events = sel.select(timeout=1)
    for key, mask in events:
        if key.data is None:
            continue
        message = key.data
        try:
            data = message.recv(1024)
           
