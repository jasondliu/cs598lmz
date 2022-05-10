import gc, weakref
from weakref import WeakValueDictionary
from threading import Thread, Lock
import struct

print_mutex = Lock()

class Client(Thread):
    def __init__(self, sock, address):
        Thread.__init__(self)
        self.sock = sock
        self.address = address
        self.size = 1024
        self.is_running = True
        self.is_alive = False
        self.name = None
        self.last_update = time.time()
        self.last_ping_time = time.time()
        self.ping_time = 0
        self.ping_times = list()
        self.ping_times_max_size = 10

    def run(self):
        self.is_alive = True
        while self.is_running:
            self.last_update = time.time()
            try:
                data = self.sock.recv(self.size)
                if not data:
                    print("Not data")
                    self.stop()
                    break
                else:
                    try:
                       
