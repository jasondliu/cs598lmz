import socket
import threading
from _thread import *
import os
import time


def thread_function(client):
    file_name = client.recv(1024).decode()
    if file_name == "quit":
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        return
    print(file_name)
    client.send(bytes("ack", 'UTF-8'))
    file_size = int(client.recv(1024).decode())
    if file_size == 0:
        client.shutdown(socket.SHUT_RDWR)
        client.close()
        return
    print(file_size)
    client.send(bytes("ack", 'UTF-8'))

