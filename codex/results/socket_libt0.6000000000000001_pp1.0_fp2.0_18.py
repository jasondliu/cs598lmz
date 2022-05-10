import socket
import sys
import os
import time
from multiprocessing import Process

TARGET = ('127.0.0.1', 9000)

def process_client(sock, target):
    while True:
        data = sock.recv(1024)
        if not data:
            break
        sock.sendall(data)
        print('[%s] %s' % (target, data))
    sock.close()
    print('close connection')

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(TARGET)
    sock.listen(1)
    print('listening on %s:%s' % TARGET)

    while True:
        client, addr = sock.accept()
        print('new connection from %s:%s' % addr)
        p = Process(target=process_client, args=(client, addr))
        p.start()
