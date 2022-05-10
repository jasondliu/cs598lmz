import socket
import time
import sys
import os

def main():
    HOST = 'localhost'
    PORT = 9999
    BUFFER_SIZE = 1024
    MESSAGE = "Hello, World!"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.sendall(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()

