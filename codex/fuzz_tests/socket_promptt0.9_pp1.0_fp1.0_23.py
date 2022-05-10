import socket
# Test socket.if_indextoname()

from socket import socket, inet_aton, inet_ntoa, \
    AF_INET, SOCK_STREAM, gethostbyname, gethostname
from errno import WSAEINVAL
from random import randint

import _socket
_socket.if_indextoname

def _if_indextoname(buf):
    # create an IPv4 (AF_INET) socket
    s = socket(AF_INET, SOCK_STREAM)
    idx = randint(1, 255)
    buf = _socket.if_indextoname(idx, buf)
    if not buf:
        raise socket.error('index %d not found' % idx)
    if len(buf) != idx:
        raise socket.error('index %d out of bounds' % idx)
    return buf

# buf must be a bytearray, and buf should be long enough to support
# the index, otherwise a buffer overflow might occur.
buf = bytearray(20)

def test_if_indexton
