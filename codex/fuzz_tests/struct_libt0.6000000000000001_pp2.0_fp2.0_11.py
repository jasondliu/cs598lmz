import _struct
import datetime
import os
import psutil
import socket
import sys
import threading
import time
import traceback

#==================================================

def get_client_address(client_socket):
    return client_socket.getpeername()

#==================================================

class SocketWrapper(object):
    def __init__(self, sock):
        self._sock = sock
        self._sock_file = sock.makefile()

    def recv(self, *args):
        return self._sock.recv(*args)

    def sendall(self, *args):
        return self._sock.sendall(*args)

    def close(self):
        self._sock.close()

    def fileno(self):
        return self._sock.fileno()

    def readline(self):
        return self._sock_file.readline()

    def readlines(self):
        return self._sock_file.readlines()

    def read(self, *args):
        return self._sock_file.read(*args)
