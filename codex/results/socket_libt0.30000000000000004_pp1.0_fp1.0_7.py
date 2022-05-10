import socket
import sys
import threading
import time

def read_from_server(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            print('\nDisconnected from the server')
            sys.exit()
        else:
            print(data.decode())

def write_to_server(sock):
    while True:
        msg = input()
        sock.send(msg.encode())

def main():
    if len(sys.argv) != 3:
        print('Usage: python3 client.py <server IP> <port>')
        sys.exit()

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((sys.argv[1], int(sys.argv[2])))
    print('Connected to the server')

    thread_read = threading.Thread(target=read_from_server, args=(sock,))
    thread_read.start()

    thread_write = threading.Thread(target=write
