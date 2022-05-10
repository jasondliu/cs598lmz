import socket
import struct
import logging
import time

from . import utils

logger = logging.getLogger(__name__)

class UDPServer(object):
    def __init__(self, port, callback, max_packet_size=1500):
        self.port = port
        self.callback = callback
        self.max_packet_size = max_packet_size
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sock.bind(('', port))
        self.running = True

