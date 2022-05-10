import select
# Test select.select()

import socket

# HOST = '127.0.0.1'
HOST = '10.211.55.20'
PORT = 9999

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connection_list = [server_socket]
