import socket
import threading
import time
import sys
import os

def recv_msg(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(data.decode())
        except:
            pass

os.system('cls')
