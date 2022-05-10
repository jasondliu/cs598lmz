import socket
import threading
import time
import os
import sys
import struct

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send_msg(self, msg):
        self.sock.send(msg)

    def recv_msg(self):
        return self.sock.recv(1024)

    def close(self):
        self.sock.close()

def main():
    if len(sys.argv) != 3:
        print("Usage: ./client.py <host> <port>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])

    client = Client(host, port)

    while True:
        msg = input("Enter a message: ")
        client.send_msg(msg.encode())
        print(client.recv_msg().decode())
