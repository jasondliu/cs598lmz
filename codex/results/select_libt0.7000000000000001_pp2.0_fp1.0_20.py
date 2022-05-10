import selectors
import sys
import time

from datetime import datetime


def check_port():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect(('localhost', 9999))
        return True
    except socket.error:
        return False


def send(message):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))
    s.sendall(str.encode(message))
    s.close()


def read():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 9999))
    return s.recv(1024).decode('utf-8')


def send_and_read(message):
    send(message)
    return read()


def main():
    if check_port():
        print("Server is running")
    else:
        print("Server
