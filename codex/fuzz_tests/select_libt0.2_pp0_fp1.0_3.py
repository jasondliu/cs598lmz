import select
import socket
import sys
import threading
import time

from . import config
from . import log
from . import util
from . import version

logger = log.get_logger(__name__)

class Server(object):
    def __init__(self, config_file):
        self.config = config.load_config(config_file)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.config['host'], self.config['port']))
        self.sock.listen(5)
        self.sock.setblocking(0)
        self.clients = {}
        self.client_lock = threading.Lock()
        self.running = True
        self.inputs = [self.sock]
        self.outputs = []
        self.message_queue = {}
        self.message_queue
