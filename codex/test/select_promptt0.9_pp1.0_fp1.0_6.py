import select
# Test select.select.

import sys
import socket
import time

# Some constants
HOST = '127.0.0.1'
SERVER_PORT = 65432
CLIENT_PORT = 65433
DATA = b'BUMP' + b'1' * 100 * 1024
TIMEOUT = 2

# Setup a simple server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, SERVER_PORT))
server_socket.listen(socket.SOMAXCONN)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
client_socket.bind((HOST, CLIENT_PORT))
client_socket.listen(socket.SOMAXCONN)

# Define a synchronous server that e
