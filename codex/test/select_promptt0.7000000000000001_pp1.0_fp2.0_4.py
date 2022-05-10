import select
# Test select.select with a socket.
#
# This is a separate program because it's only available on some
# platforms.

import socket
import os
import time
import sys
import select
import threading

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 0))
    s.listen(2)
    return s

def start_client(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", port))
    return s

def main(start_server, start_client):
    port = start_server().getsockname()[1]
    s = start_client(port)
    s.send("x")
    time.sleep(1)
    s.close()
