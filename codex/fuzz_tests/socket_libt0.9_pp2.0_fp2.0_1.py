import socket
import time

TIMEOUT = 0.1

def read(s, l=128):
    return s.read(l)

def read_until(s, pattern, l=128):
    return s.read_until(pattern, l)

def send(s, data, debug = False):
    if debug: print '[DEBUG] send : ', data
    return s.send(data)

def recv(s, l=128, debug = False):
    data = s.recv(l)
    if debug: print '[DEBUG] recv : ', data
    return data

def recv_until(s, pattern, l=128, debug = False):
    data = s.recv_until(pattern, l)
    if debug: print '[DEBUG] recv : ', data
    return data

def close(s):
    return s.close()

def check(s, debug = False):
    data = recv(s)
    if debug: print '[DEBUG] check : [%s]' % data
    if data == None:
        return 1


