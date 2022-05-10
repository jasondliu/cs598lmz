import selectors
import socket
import sys
import threading
import time
import traceback

from . import metadata
from . import util

def _make_logger():
    return logging.getLogger(__name__)

def _make_thread_name(name):
    return '{}-{}'.format(name, threading.current_thread().name)

def _make_thread_name_for_read(name):
    return _make_thread_name('{}-read'.format(name))

def _make_thread_name_for_write(name):
    return _make_thread_name('{}-write'.format(name))

class _Connection:
    def __init__(self, sock, addr, callback, logger):
        self.sock = sock
        self.addr = addr
        self.callback = callback
        self.logger = logger
        self.sock_file = sock.makefile('rb')
        self.read_buffer = b''
        self.write_buffer = []
