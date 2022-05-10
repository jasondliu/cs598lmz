import select
import socket
import sys
import time
import threading
import traceback
import Queue

import config
import util

class Connection(object):
    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.buf = ''
        self.closed = False
        self.last_activity = time.time()
        self.send_queue = Queue.Queue()
        self.send_lock = threading.Lock()
        self.send_thread = threading.Thread(target=self.send_loop)
        self.send_thread.daemon = True
        self.send_thread.start()

    def send(self, data):
        self.send_queue.put(data)

    def send_loop(self):
        while not self.closed:
            try:
                data = self.send_queue.get(timeout=0.1)
            except Queue.Empty:
                continue
