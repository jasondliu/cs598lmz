import select
import socket
import sys
import threading
import time
from queue import Queue

import paramiko

SSH_PORT = 22
DEFAULT_PORT = 4000
BUF_SIZE = 1024

g_verbose = True


def handler(chan, host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
    except Exception as e:
        verbose('Forwarding request to %s:%d failed: %r' % (host, port, e))
        return

    verbose(
        'Connected!  Tunnel open %r -> %r -> %r' %
        (chan.origin_addr, chan.getpeername(), (host, port)))
    while True:
        r, w, x = select.select([sock, chan], [], [])
        if sock in r:
            data = sock.recv(BUF_SIZE)
            if len(data) == 0:
                break
            chan.send(data)
        if chan in r:
            data = chan.rec
