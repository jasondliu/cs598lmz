import socket
import sys
import time
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def handle_client(client_connection):
    while True:
        data = client_connection.recv(16)
        print('received {!r}'.format(data))
        if data:
            print('sending data back to the client')
            client_connection.sendall(data)
        else:
            print('no data from', client_address)
            break
    client_connection.close()

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)
    handle_client(connection)
