import socket
import telnetlib
import time

from nclib import netcat

class Vulnerable(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = None

    def recvuntil(self, until):
        output = b""
        while True:
            data = self.sock.recv(1)
            output += data
            if data.decode("utf-8") == until:
                break
        return output

    def recvline(self):
        return self.recvuntil("\n")

    def recvlines(self, amount):
        return [self.recvline() for _ in range(amount)]

    def recvbytes(self, amount):
        return self.sock.recv(amount)

    def sendline(self, line):
        self.sock.send("{}\n".format(line).encode("utf-8"))

    def send(self, data):
        self.sock.send(data)

