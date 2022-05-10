import socket

# IpAddress = '192.168.10.11'
IpAddress = '127.0.0.1'
PortNumber = 8888


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((IpAddress, PortNumber))
server_socket.listen(0)

connection, client_address = server_socket.accept()

while True:
    data = connection.recv(1024)
    if data:
        print(data.decode())
    connection.sendall(data)
