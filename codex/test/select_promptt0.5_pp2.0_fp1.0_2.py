import select
# Test select.select() on a socket that is closed by the server.
import unittest
from test import test_support
import socket
import time

HOST = test_support.HOST

def server(evt, serv):
    conn, addr = serv.accept()
