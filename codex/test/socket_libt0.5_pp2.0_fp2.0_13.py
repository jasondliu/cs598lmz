import socket
import time
import sys

def send_msg(sock, msg):
    sock.send(msg.encode())
    print("send: ", msg)

def recv_msg(sock):
    data = sock.recv(1024)
    msg = data.decode()
    print("recv: ", msg)
    return msg

def send_msg_to_server(sock, msg):
    send_msg(sock, msg)
    recv_msg(sock)

def login(sock):
    send_msg(sock, "LOGIN")
    send_msg(sock, "admin")
    send_msg(sock, "admin")

def logout(sock):
    send_msg(sock, "LOGOUT")

def add_user(sock, user, password):
    send_msg(sock, "ADD")
    send_msg(sock, user)
    send_msg(sock, password)

