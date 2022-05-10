import socket
import sys
import threading

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print('Received {}'.format(request))
    client_socket.send('ACK!')
    client_socket.close()

while True:
    # Wait for a connection
    print('waiting for a connection')
    client, address = sock.accept()
    print('connection from', address)
    client_handler = threading.Thread(
        target=handle_client,
        args=(client,)
    )
    client_handler.start()
