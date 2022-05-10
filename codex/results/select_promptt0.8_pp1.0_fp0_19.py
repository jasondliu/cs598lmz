import select
# Test select.select()
import sys
import threading
import time
from struct import pack, unpack
from socket import AF_INET, socket, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from pyp2p.net import *


def test_recv():
    # size = 1000
    # ip = "192.168.0.39"
    # port = 30000
    # addr = (ip, port)

    # sock = socket(AF_INET, SOCK_STREAM)
    # sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # sock.bind(addr)
    # sock.listen(5)

    # packed_data = pack('I', size)
    # conn, addr = sock.accept()
    # conn.sendall(packed_data)
    # time.sleep(1)
    # conn.sendall(b'hello')
    # data, addr = conn.recvfrom(size)

    # print(unpack('I', data))

    # Test Data
