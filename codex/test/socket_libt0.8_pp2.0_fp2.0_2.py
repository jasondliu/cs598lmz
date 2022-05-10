import socket
import sys
import os

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 1337        # Port to listen on (non-privileged ports are > 1023)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


def get_summary():
    with open("summary.txt", "r") as f:
        return f.read()
    

def get_files_to_send():
    files = []
    for file in os.listdir("files_to_send"):
        files.append(file)
    return files


def send_summary():
    s.sendall(str.encode(get_summary()))


def send_file(file):
    filename = file
    f = open("files_to_send/"+filename, "rb")
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)

