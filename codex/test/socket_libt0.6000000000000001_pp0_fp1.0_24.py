import socket
import sys
import threading
import time

s = None

def server():
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('0.0.0.0', 3333))
    s.listen(1)
    conn, addr = s.accept()
