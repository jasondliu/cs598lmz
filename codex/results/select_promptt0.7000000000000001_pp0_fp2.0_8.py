import select
# Test select.select() with multiple channels, non-blocking mode.
import socket
import sys
import thread
import time
import unittest

from test import test_support

HOST = test_support.HOST
SERVER_PORT = test_support.find_unused_port()

def ServerThread(test, serve_once, server_addr):
    """Sets up a server that listens on server_addr, and either serves one
       connection (serve_once is true), or continues to serve forever."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(server_addr)
    s.listen(5)
    while True:
        test.server_started.set()
        conn, addr = s.accept()
        if serve_once:
            break
    conn.sendall(b"x")
    conn.close()
    if serve_once:
        s.close()

def Client
