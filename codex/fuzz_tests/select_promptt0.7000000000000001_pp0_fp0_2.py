import select
# Test select.select()
import socket
import sys
import time
import types
# Test asyncore.dispatcher.send()
import unittest
# Support for testing asyncore classes

from test.test_support import run_unittest

HOST = 'localhost'
PORT = 50007

class EchoServer(asyncore.dispatcher):

    def __init__(self, address, map=None):
        asyncore.dispatcher.__init__(self, map=map)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.bind(address)
        self.listen(1)

    def handle_accept(self):
        conn, addr = self.accept()
        EchoHandler(conn)

class EchoHandler(asyncore.dispatcher):

    def __init__(self, conn):
        asyncore.dispatcher.__init__(self, conn)
        self.buffer = ''

    def handle_read(self):
        self.buffer = self.recv(8192)
