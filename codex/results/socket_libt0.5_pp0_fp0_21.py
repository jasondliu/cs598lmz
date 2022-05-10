import socket
import sys
import threading
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 5555))
s.sendall(b"Hello, world")
s.close()
