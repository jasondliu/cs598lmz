import selectors

import logging
import argparse
import sys
import os
import signal
import time

from collections import deque
from threading import Thread, Event

from . import utils

logger = logging.getLogger(__name__)

class Server(object):
    def __init__(self, host, port, backlog=50):
        self.host = host
        self.port = port
        self.backlog = backlog
        self.server_socket = None
        self.server_thread = None
        self.server_running = Event()
        self.server_stopped = Event()
        self.server_stopped.set()
        self.client_handlers = {}
        self.client_handler_threads = {}
        self.client_handler_threads_running = {}
        self.client_handler_threads_stopped = {}

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
