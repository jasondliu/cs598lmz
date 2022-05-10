import socket
import threading
import time
import sys
import os

# TCP_IP = '192.168.0.88' #Server IP
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

def recv_data():
    # print("recv_data")
    while 1:
        data = s.recv(1024)
        if not data:
            print("server socket close")
            break
        print("recv:", data.decode())

def send_data():
    # print("send_data")
    while 1:
        data = input("input(type 'exit' to quit): ")
        if data == 'exit':
            print("exit")
            s.close()
            os._exit(0)
        s.send(data.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

