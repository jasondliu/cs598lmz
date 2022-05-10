import mmap
import sys
import time
import threading

class DataRecorder:
    def __init__(self, path, size, init_val=0.0, name=None):
        self.size = size
        self.name = name
        self.path = path
        self.data = [init_val] * size
        self.lock = threading.Lock()
        self.started = False
        self.file = None
        self.mm = None
        self.stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True

    def start(self):
        self.stop_event.clear()
        self.thread.start()

    def stop(self):
        self.stop_event.set()
        self.thread.join()

    def run(self):
        while not self.stop_event.is_set():
            self.lock.acquire()
