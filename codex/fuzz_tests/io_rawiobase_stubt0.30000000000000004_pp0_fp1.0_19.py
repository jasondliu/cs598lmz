import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file is not None:
            self.file.close()
            self.file = None
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, type, value, traceback):
        self.close()
    def readable(self):
        return True
    def readinto(self, b):
        return self.file.readinto(b)

import os
import sys
import time
import socket
import select
import errno
import signal
import logging
import threading
import multiprocessing
import multiprocessing.connection
import multiprocessing.reduction
import multiprocessing.managers
import multiprocessing.util
import multiprocessing.pool
import multiprocessing.queues
import multiprocessing.synchronize
import multiprocessing
