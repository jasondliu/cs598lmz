import select
# Test select.select()

# Create a pair of connected sockets

import socket
import sys

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 0))
server.listen(1)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server.getsockname())

# Wait for a single connection

print('starting up on %s port %s' % server.getsockname())
connection, client_address = server.accept()
try:
    print('client connected:', client_address)
    while True:
        r, w, e = select.select([connection], [], [], 1)
        if r:
            data = connection.recv(1024)
            if data:
                connection.sendall(data)
            else:
                break
finally:
    connection.close()
    server.close()
