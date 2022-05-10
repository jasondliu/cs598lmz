import select
# Test select.select() with a pipe and a socket.
import socket
import sys
import time

def make_connection():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 0))
    s.listen(1)
    conn, addr = s.accept()
    return conn

def test():
    conn = make_connection()
    r, w = os.pipe()
    inputs = [r, conn]
    outputs = []
