import socket
import time

TIMEOUT = 0.1

def read(s, l=128):
    return s.read(l)

def read_until(s, pattern, l=128):
    return s.read_until(pattern, l)

