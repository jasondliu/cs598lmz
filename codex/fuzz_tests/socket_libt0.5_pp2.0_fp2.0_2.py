import socket
import sys
import os
import time

host = '127.0.0.1'
port = 9999

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send('USER username'.encode('utf-8'))
    s.send('PASS password'.encode('utf-8'))
    return s

def send_commands(s, cmd):
    cmd = cmd.rstrip()
    s.send(cmd.encode('utf-8'))
    recv_len = 1
    response = ""
    while recv_len:
        data = s.recv(4096)
        recv_len = len(data)
        response += data.decode('utf-8')
        if recv_len < 4096:
            break
    return response

def main():
    s = connect()
    while True:
        cmd = input("Enter command: ")
        if cmd == 'exit':
            s.close()
