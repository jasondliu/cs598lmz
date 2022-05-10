import select
# Test select.select ()

# Example 8.16 select_echo_server.py
from socket import *
import select
import time

tasks = []

to_read = {}  # Mapping sockets -> tasks (generators)
to_write = {}  # Mapping sockets -> tasks (generators)

def server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        yield ('read', server_socket)
        client_socket, addr = server_socket.accept() # task blocks
        print('Connection from', addr)
        tasks.append(client(client_socket))

def client(client_socket):
    while True:
        yield ('read', client_socket)
        request = client_socket.recv(4096) # task blocks
        if not request:
            break
        else:
            response = 'Hello world\n
