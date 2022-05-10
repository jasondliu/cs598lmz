import socket
import time
import sys
import os
import re

def usage():
    print("Usage: python3 " + sys.argv[0] + " <host> <port>")
    sys.exit(1)

if len(sys.argv) != 3:
    usage()

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

def recv(s):
    data = s.recv(1024)
    return data.decode("utf-8")

def recv_until(s, string):
    data = ""
    while string not in data:
        data += recv(s)
    return data

def send(s, string):
    s.send(string.encode("utf-8"))

def sendline(s, string):
    send(s, string + "\n")

def interactive(s):
    print("Got interactive shell!")
   
