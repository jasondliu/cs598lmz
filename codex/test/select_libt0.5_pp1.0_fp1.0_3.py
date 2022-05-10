import select
import socket
import sys
import threading
import time

import websocket


#
# Keeps track of the number of connections and their state.
#
class ConnectionState(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.connections = 0
        self.connections_max = 0

    def inc(self):
        self.lock.acquire()
        self.connections += 1
        if self.connections > self.connections_max:
            self.connections_max = self.connections
        self.lock.release()

    def dec(self):
        self.lock.acquire()
        self.connections -= 1
        self.lock.release()

    def get(self):
        self.lock.acquire()
        ret = self.connections
        self.lock.release()
        return ret

    def get_max(self):
        self.lock.acquire()
        ret = self.connections_max
        self.lock.release()
        return ret


#
