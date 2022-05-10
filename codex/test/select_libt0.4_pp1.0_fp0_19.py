import select
import socket
import sys
import threading
import time
import traceback

import pytest

import curio
from curio import *
from curio import _core
from curio.socket import *
from curio.traps import *

from utils import *

def test_socket_create_close(kernel):
    sock = socket.socket()
    sock.setblocking(False)
    sock.bind(('127.0.0.1', 0))
    sock.listen(5)
    csock = socket.socket()
    csock.setblocking(False)
    csock.connect(sock.getsockname())

    async def server_task():
        sock = await open_tcp_server('127.0.0.1', 0)
        client_sock, addr = await sock.accept()
        await client_sock.send(b'ABC')
        await client_sock.close()
        await sock.close()

