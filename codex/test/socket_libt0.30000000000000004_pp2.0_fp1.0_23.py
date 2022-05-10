import socket
import threading
import sys
import time

# Set up the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
s.bind(server_address)

# Listen for incoming connections
s.listen(5)

# Accept the connection
connection, client_address = s.accept()
print('connection from', client_address)

# Receive the data in small chunks and retransmit it
while True:
    data = connection.recv(16)
    print('received "%s"' % data)
    if data:
        print('sending data back to the client')
        connection.sendall(data)
    else:
        print('no more data from', client_address)
        break

# Clean up the connection
connection.close()
