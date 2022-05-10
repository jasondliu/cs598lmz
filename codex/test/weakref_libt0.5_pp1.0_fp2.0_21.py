import weakref
import pickle

from diesel import Service, Loop, ConnectionClosed, send, sleep, until_eol, first, last, wait
from diesel.util.queue import Queue
from diesel.util.event import Event
from diesel.util.pool import Pool
from diesel.protocols.redis import RedisServer, RedisClient
from diesel.util.event import Event
from diesel.util.queue import Queue

from diesel.util.pool import Pool

class RedisConnection(RedisClient):
    def __init__(self, conn):
        self.conn = conn
        self.q = Queue()
        self.closed = False
        self.closed_event = Event()
        self.closed_event.set()

    def _write(self, data):
        self.conn.write(data)

    def _read(self, n):
        return self.conn.read(n)

    def close(self):
        self.closed = True
        self.conn.close()
        self.closed_event.set()

