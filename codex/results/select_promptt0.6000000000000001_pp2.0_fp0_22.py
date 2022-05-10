import select
# Test select.select
import socket
import sys
import time

try:
    import thread
except ImportError:
    import _thread as thread

from test import test_support

HOST = test_support.HOST

def server(evt, serv, serv2):
    # Test accept()
    conn, addr = serv.accept()
    conn.close()
    serv.close()

    # Test accept() after setblocking(0)
    serv2.setblocking(0)
    conn, addr = serv2.accept()
    conn.close()
    serv2.close()

    # Test that we can select() for a socket service created with
    # socket.socket()
    sock = socket.socket()
    sock.bind((HOST, 0))
    sock.listen(5)
    r, w, e = select.select([sock],[],[],5)
    if sock not in r:
        raise TestFailed, "socket object not returned by select"
    sock.close()

    # Test that we can select() for a socket service created with
    # socket.socket(
