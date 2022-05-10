import select
import socket
import sys
import threading
import time
import traceback
import Queue

from util import *
from common import *

class AsyncSocket(object):
    def __init__(self, sock, sock_type, sock_family, sock_proto):
        self.sock = sock
        self.sock_type = sock_type
        self.sock_family = sock_family
        self.sock_proto = sock_proto
        self.send_queue = Queue.Queue()
        self.recv_queue = Queue.Queue()
        self.send_thread = None
        self.recv_thread = None
        self.send_thread_running = False
        self.recv_thread_running = False
        self.send_thread_lock = threading.Lock()
        self.recv_thread_lock = threading.Lock()
        self.closed = False

