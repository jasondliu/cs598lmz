import socket
import struct
import time
import json
from contextlib import closing

from lib.ThreadManager import ThreadManager
from lib.ThreadManager import ThreadBase
from lib.Logger import Logger

from conf import conf
from conf import set_log
from conf import set_bgp

class BGPSession(ThreadBase):
    def __init__(self, config, thread_manager):
        ThreadBase.__init__(self)
        self.config = config
        self.thread_manager = thread_manager
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.sock.settimeout(1.0)

        self.recv_count = 0
        self.update_count = 0
        self.open_count = 0
        self.keepalive
