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

def handle_client(client_connection):
    while True:
        data = client_connection.recv(1024)
        print(data.decode('ascii'))
        if data:
            client_connection.sendall(data)
        else:
            break

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        threading.Thread(target=handle_client, args=(connection,)).start()
    finally:

