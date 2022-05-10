import select
import socket
import sys
import threading


def client(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    while True:
        data = input("input: ")
        sock.send(data.encode("utf-8"))
        print("send: ", data)
        data = sock.recv(1024)
        print("recv: ", data.decode("utf-8"))


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen(1)
    conn, addr = sock.accept()
    while True:
        data = conn.recv(1024)
        print("recv: ", data.decode("utf-8"))
        data = input("input: ")
        conn.send(data.encode("utf-8"))
        print("send: ", data)


