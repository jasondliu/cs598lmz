import socket
import time
import threading
import sys

def send_message(sock, message):
    sock.sendall(message)

def recv_message(sock):
    data = sock.recv(1024)
    return data

def client_handler(sock):
    while True:
        data = recv_message(sock)
