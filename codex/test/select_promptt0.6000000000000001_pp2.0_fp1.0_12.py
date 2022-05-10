import select
# Test select.select function
# http://docs.python.org/3.3/library/select.html

import socket

# create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server
client_socket.connect(('127.0.0.1', 8080))

# create file object from client socket
client_file = client_socket.makefile('rwb')

# send data
client_file.write('GET / HTTP/1.0\n\n'.encode())

# check for data
data = client_socket.recv(1024)
print(data)

# close file object
client_file.close()

# close client socket
client_socket.close()
