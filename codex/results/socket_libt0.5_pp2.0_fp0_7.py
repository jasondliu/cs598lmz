import socket
import threading
import time

from . import config

logger = logging.getLogger(__name__)

class Client(threading.Thread):
    def __init__(self, server, socket_family, socket_type, socket_proto,
                 socket_address, socket_port):
        threading.Thread.__init__(self)
        self.server = server
        self.socket_family = socket_family
        self.socket_type = socket_type
        self.socket_proto = socket_proto
        self.socket_address = socket_address
        self.socket_port = socket_port
        self.running = True
        self.socket = None
        self.last_data_received = 0
        self.last_data_sent = 0
        self.last_data_received_time = 0
        self.last_data_sent_time = 0

    def run(self):
        logger.info('Client thread started')

        try:
            self.socket = socket.socket(self.socket_family, self.socket_type, self
