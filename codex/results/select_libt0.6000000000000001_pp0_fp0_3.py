import select
import socket
import sys
import time
import datetime


class Client:
    def __init__(self, ip, port, username):
        self.ip = ip
        self.port = port
        self.username = username
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.ip, self.port))
        self.socket.setblocking(False)
        self.connected = True

    def disconnect(self):
        self.socket.close()
        self.connected = False

    def send_message(self, message):
        self.socket.send(message.encode())

    def rcv_message(self):
        try:
            msg = self.socket.recv(4096)
            if msg:
                return msg.decode()
        except:
            pass


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 client.py <IP> <PORT> <USERNAME>")
        sys.exit(1)
