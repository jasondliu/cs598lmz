import socket
import sys
import time
import threading
import os
import subprocess
import signal
import re

# constants
HOST = '127.0.0.1'
PORT = 50000
BUFSIZE = 4096

# global variables
client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# functions
def connect_to_server(host, port):
    try:
        client_sock.connect((host, port))
        print('Connected to {}:{}'.format(host, port))
        return True
    except Exception as e:
        print('Failed to connect to {}:{}'.format(host, port))
        print(e)
        return False

def send_message(sock, msg):
    try:
        sock.sendall(msg.encode('utf-8'))
        print('Sent: {}'.format(msg))
        return True
    except Exception as e:
        print('Failed to send message')
        print(e)
        return False

def receive_message(s
