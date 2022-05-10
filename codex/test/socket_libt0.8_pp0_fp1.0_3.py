import socket
import sys

def chat(sock):
    while 1:
        data = raw_input("")
        if data != "":
            sock.sendall(data)
        else:
            break
        data = sock.recv(4096)
