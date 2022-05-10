import select
import sys
import time

from logger import Logger
from config import Config

class Sender:
    def __init__(self, config):
        self.config = config
        self.logger = Logger(self.config)
        self.logger.log("Sender initialized")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('', self.config.udp_port))
        self.sock.setblocking(0)
        self.last_send_time = time.time()
        self.last_recv_time = time.time()
        self.last_send_seq = 0
        self.last_recv_seq = 0
        self.last_recv_ack = 0
        self.last_send_ack = 0
        self.send_window = []
        self.recv_window = []
        self.send_window_size = self.config.window_size
        self.recv_window_size = self.config.window
