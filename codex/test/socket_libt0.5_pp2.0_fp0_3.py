import socket
import sys
import subprocess
import os

def send_file(sock, filename):
    if os.path.isfile(filename):
        f = open(filename, 'rb')
        while True:
            l = f.read(1024)
            while (l):
                sock.send(l)
                #print('Sent ',repr(l))
                l = f.read(1024)
            if not l:
                f.close()
                break
    else:
        print("file not found")

def send_cmd(sock, cmd):
    sock.send(cmd.encode())
    return sock.recv(1024).decode()

def main():
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('localhost', 10000)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

