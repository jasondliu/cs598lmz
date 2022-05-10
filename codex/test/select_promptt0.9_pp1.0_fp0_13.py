import select
# Test select.select()

# $ perldoc -f select
# [...]
# select() supports a timeout and will return a list of
# handles that are ready for reading, writing or have an exceptional
# condition pending.  It will return an empty list upon timeout. 
# [...]


import socket
from StringIO import StringIO
import sys
import os
import time

from socket_util import log

MAX_READ = 32768 # Maximum data to be read each time
MAX_BUF  = 10    # Maximum number of recv statements to be performed

def make_socket(udp, reuse_addr=True):
    # Create a UDP or TCP socket
    sock_type = socket.SOCK_DGRAM if udp else socket.SOCK_STREAM
    sock = socket.socket(socket.AF_INET, sock_type)

    if reuse_addr:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    return sock

