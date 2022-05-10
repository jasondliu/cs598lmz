import select
import socket
import sys

import pynetwork_linux.unix as unix
import pynetwork_linux.interface as interface
import pynetwork_linux.error as error

class UnixDomainServerSocket(server.ServerSocket):
    def __init__(self, sock=None, path=None, bind=True, listen=True):
        self.path = path
        self.sock = sock

        if not sock and not path:
            raise error.InvalidSocket
        
        if not sock:
            sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            sock.setblocking(False)

            if bind:
                self.bind(path)

            if listen:
                self.listen()

        self.sock = sock

        self.fileno = sock.fileno

    def bind(self, path, blocking=False):
        self.path = path
        self.sock.setblocking(blocking)
