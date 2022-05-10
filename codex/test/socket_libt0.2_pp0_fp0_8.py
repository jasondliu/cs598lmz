import socket
import sys
import time
import threading
import Queue
import random
import os
import subprocess
import signal
import re
from datetime import datetime
from datetime import timedelta

from config import *
from util import *

#
# This is the main class for the server.
#
class Server:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((HOST, PORT))
        self.sock.listen(5)
        self.clients = []
        self.client_lock = threading.Lock()
        self.client_queue = Queue.Queue()
        self.client_thread = threading.Thread(target=self.client_handler)
        self.client_thread.daemon = True
        self.client_thread.start()
        self.server_thread = threading
