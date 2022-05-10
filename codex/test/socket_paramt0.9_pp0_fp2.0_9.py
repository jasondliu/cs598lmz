import socket
socket.if_indextoname(3)

from server import IdProvider
from queue import Queue
from threading import Thread, Event
import time
from wrapper import Timer
from struct import Struct


recv_qs = Queue(10)
replay_qs = Queue(10)
snd_event = Event()
replay_event = Event()
NOTARY_ADDR = ('notary.csail.mit.edu', 3410)

def receive():
    def _fn():
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            _, snd_port = sock.getsockname()
            sock.bind(('', snd_port))
            addr = sock.getsockname()
            while True:
                data, addr = sock.recvfrom(1500)
                recv_qs.put(data[8:])
                # print(data)
    return _fn

