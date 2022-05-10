import socket
import time

def send_cmd(cmd):
    # send command to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(cmd)
    s.close()

def send_cmd_with_reply(cmd):
    # send command to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(cmd)
    reply = s.recv(1024)
    s.close()
    return reply

def send_cmd_with_reply_and_wait(cmd):
    # send command to the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.send(cmd)
    reply = s.recv(1024)
    time.sleep(1)
    reply = s.recv(1024)
    s
