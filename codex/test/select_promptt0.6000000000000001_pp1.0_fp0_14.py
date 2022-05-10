import select
# Test select.select
# https://docs.python.org/3.3/library/select.html
# https://docs.python.org/3/library/select.html
# https://docs.python.org/3/library/select.html
# https://docs.python.org/3/library/select.html

import time
import threading

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(5)
    # print("Server listening on port 5000")
    while True:
        client_socket, address = server_socket.accept()
        print("Client connected")
        # client_socket.sendall(b"Welcome to the server")
        # print("Sent welcome message")
        # data = client_socket.recv(1024)
        # print("Received {}".format(data))
        # client_socket.close()

