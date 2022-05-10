import socket
import threading
import time
import sys
import os

# global variables
HOST = ''
PORT = 50000
BUFSIZE = 4096

# create socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind socket
server.bind((HOST, PORT))

# listen
server.listen()

# client list
clients = []

# lock
lock = threading.Lock()

def broadcast(msg):
    with lock:
        for client in clients:
            client.send(msg)

def handler(client, addr):
    with lock:
        clients.append(client)

    try:
        while True:
            msg = client.recv(BUFSIZE)
            if not msg:
                break
            broadcast(msg)
    except Exception as e:
        print(e)
    finally:
        client.close()

    with lock:
        clients.remove(client)

while True:
    # accept
    client, addr = server.accept()
