import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('data.db')
import time

BUF_SIZE = 256
ARRAY_SIZE = BUF_SIZE * 10

class Worker(threading.Thread):
    def __init__(self, c_buffer, c_size, c_array, c_array_size, semaphore, lock):
        super(Worker, self).__init__()
        self.c_buffer = c_buffer
        self.c_size = c_size
        self.c_array = c_array
        self.c_array_size = c_array_size
        self.semaphore = semaphore
        self.lock = lock


    def run(self):
        # Python side
        libc = ctypes.CDLL(ctypes.util.find_library('c'))

        while True:
            self.semaphore.acquire()
            # libc.printf("%s\n", self.c_buffer).decode('utf-8')
            utf8_string = ctypes.cast(self.c_buffer, ctypes.c_char_p
