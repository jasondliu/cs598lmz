import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('192.168.12.1', 5000)
sock.bind(server_address)
print('starting up on {} port {}'.format(*server_address))
sock.listen(1)

try:
    while True:
        print('waiting for a connection')
        connection, client_address = sock.accept()
        try:
            print('client connected:', client_address)
            while True:
                data = connection.recv(16)
                print('received {!r}'.format(data))
                if data:
                    print('sending data back to the client')
                    connection.sendall(data)
                else:
                    print('no data from', client_address)
                    break
        finally:
            connection.close()
finally:
    sock.close()
