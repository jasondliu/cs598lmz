import select
# Test select.select() with a socket object.
import socket
import time

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 0))
    s.listen(1)
    s.setblocking(0)
