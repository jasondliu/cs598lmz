import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
        self.file = open(self.name, self.mode)
    def writable(self):
        return True
    def readable(self):
        return True
    def readinto(self, buffer):
        return self.file.readinto(buffer)
    def write(self, buffer):
        return self.file.write(buffer)
    def close(self):
        return self.file.close()
    def flush(self):
        return self.file.flush()
    def tell(self):
        return self.file.tell()

def create_file(name, mode):
    return File(name, mode)


import os
import sys
import io
import time
import socket
import array
import logging
import threading
import traceback
import argparse
import subprocess
import multiprocessing
from functools import partial
import pyaudio
sys.path.append(os.path.join(os.path.dirname(__file__), '
