import mmap
import struct
import sys
import os

class shm_exception(Exception):
    pass

class shm_file(object):
    def __init__(self, name):
        self.name = name
