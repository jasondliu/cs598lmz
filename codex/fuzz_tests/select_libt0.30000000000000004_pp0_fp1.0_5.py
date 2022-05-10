import select
import socket
import sys
import threading
import time
import traceback

from . import config
from . import log
from . import util
from . import version
from . import x509

class Client(object):
    def __init__(self, config):
        self.config = config
        self.log = log.get_logger(config)

        self.hostname = config.hostname
        self.port = config.port
        self.username = config.username
        self.password = config.password
        self.ca_certs = config.ca_certs
        self.insecure = config.insecure
        self.server_host_key = config.server_host_key
        self.client_keys = config.client_keys
        self.client_certs = config.client_certs
        self.server_host_key_algs = config.server_host_key_algs
        self.kex_algs = config.kex_algs
        self.ciphers = config.ciphers
        self.macs = config.
