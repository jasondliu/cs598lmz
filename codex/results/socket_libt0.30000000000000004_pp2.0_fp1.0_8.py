import socket
import sys
import threading
import time
import traceback

from . import __version__
from . import config
from . import log
from . import utils

logger = log.get_logger(__name__)


class Server(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = config.load_config(config_file)
        self.listen_host = self.config.get('listen_host', '127.0.0.1')
        self.listen_port = self.config.get('listen_port', 8080)
        self.listen_address = (self.listen_host, self.listen_port)
        self.server_name = self.config.get('server_name', 'socks5')
        self.server_version = self.config.get('server_version', __version__)
        self.server_banner = self.config.get('server_banner', 'socks5')
        self.server_banner
