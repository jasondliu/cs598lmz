import select
import os
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8002))
server_socket.listen(5)

poll_object = select.poll()
poll_object.register(server_socket, select.POLLIN)

sockets_dict = {}

while True:
    poll_list = poll_object.poll(1)
    for fd, event in poll_list:
        if fd == server_socket.fileno():
            client_socket, client_address = server_socket.accept()
            client_socket.setblocking(False)
            poll_object.register(client_socket, select.POLLIN)
