import select
# Test select.select(). The selects work on single connections,
# but not on a group of connections.

import errno
import socket
import os
import time
import sys

HOST = ''
PORT = 54321
NUM = 4
NUM1 = 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)

def get_open_port():
    global PORT
    PORT = PORT + 1
    return PORT

def get_connections(n):
    conns = []
    for i in range(n):
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        PORT = get_open_port()
        cs.connect((HOST, PORT))
        conns.append(cs)
    return conns

def test():
    clients = get_connections(NUM)

