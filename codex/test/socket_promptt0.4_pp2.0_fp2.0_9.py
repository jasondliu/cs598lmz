import socket
# Test socket.if_indextoname()
import sys
import threading
import time
import unittest

from test import support

HOST = support.HOST

if hasattr(socket, 'SOCK_NONBLOCK'):
    SOCK_NONBLOCK = socket.SOCK_NONBLOCK
else:
    SOCK_NONBLOCK = os.O_NONBLOCK

if hasattr(socket, 'SOCK_CLOEXEC'):
    SOCK_CLOEXEC = socket.SOCK_CLOEXEC
else:
    SOCK_CLOEXEC = 0o2000000

if hasattr(socket, 'SOCK_NOSIGPIPE'):
    SOCK_NOSIGPIPE = socket.SOCK_NOSIGPIPE
else:
    SOCK_NOSIGPIPE = 0o4000000

if hasattr(socket, 'SOCK_EXCL'):
    SOCK_EXCL = socket.SOCK_EXCL
else:
    SOCK_EXCL = 0o10000000

