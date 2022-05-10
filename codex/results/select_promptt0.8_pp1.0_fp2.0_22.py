import select
# Test select.select for reading and writing.

def verbose(*args):
    if verbose: print(args)

import socket
import errno

def trywrite(sock, data, desc=None):
    while data:
        try:
            n = sock.send(data)
        except socket.error as e:
            if e.args[0] != errno.EAGAIN:
                raise
            verbose("trywrite", desc, "blocking")
            select.select([], [sock], [])
            verbose("trywrite", desc, "continuing")
        else:
            data = data[n:]

def tryread(sock, n, desc=None):
    chunks = []
    while n > 0:
        try:
            data = sock.recv(n)
        except socket.error as e:
            if e.args[0] != errno.EAGAIN:
                raise
            verbose("tryread", desc, "blocking")
            select.select([sock], [], [])
            verbose("tryread", desc, "contin
