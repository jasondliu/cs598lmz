import socket
import sys
import time

from config import *
from data import *
from struct_pack import *


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.sock.setblocking(0)

    def send_msg(self, msg):
        self.sock.send(msg)

    def recv_msg(self):
        return self.sock.recv(1024)


def send_msg(client, msg):
    client.send_msg(msg)
    print('send msg : ', msg)


def recv_msg(client):
    try:
        data = client.recv_msg()
        print('recv msg : ', data)
        return data
    except socket.error as e:
        print('recv error : ', e)
        return None


