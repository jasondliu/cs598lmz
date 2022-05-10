import socket
# Test socket.if_indextoname()

import os
import sys
import time
import unittest
import subprocess
import platform

from test_support import run_unittest, reap_children, get_attribute

HOST = 'localhost'
PORT = 50007

class NetworkConnectionNoServer(Exception):
    pass

def start_server(addr, family):
    if family == socket.AF_INET:
        server = socket.socket(family, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(addr)
        server.listen(1)
        conn, addr = server.accept()
        server.close()
        return conn
    elif family == socket.AF_INET6:
        # IPv6 sockets can't listen and connect at the same time
        # so we create a listening socket in a separate process
        # and connect to it.
        cmd = [sys.executable, '-u', '-c',
               'import socket,sys;s=socket.
