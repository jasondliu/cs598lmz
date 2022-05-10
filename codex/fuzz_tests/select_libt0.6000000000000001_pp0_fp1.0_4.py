import select
import socket
import sys
import threading
import time
import os

#------------------------------------------------------------------------------

class BaseConnection(object):

    def __init__(self, host, port, config):
        self.config = config
        self._host = host
        self._port = port
        self._thread = None
        self._sock = None
        self._sock_out = None
        self._sock_in = None
        self._sock_err = None
        self._sock_in_buf = ''
        self._sock_err_buf = ''
        self._sock_in_sem = threading.Semaphore(0)
        self._sock_err_sem = threading.Semaphore(0)
        self._sock_connected_sem = threading.Semaphore(0)
        self._sock_connected = False
        self._sock_closed = False
        self._sock_in_closed = False
        self._sock_err_closed = False
        self._sock_recv_lock = threading.Lock()
