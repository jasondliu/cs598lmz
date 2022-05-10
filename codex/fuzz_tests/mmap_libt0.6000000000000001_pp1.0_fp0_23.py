import mmap
import shutil
import os

from . import const
from . import utils
from . import data

class File:
    def __init__(self, filename=None, mode='r'):
        self.filename = filename
        self.mode = mode
        self.fd = None
        if filename:
            self.open(filename, mode)

    def open(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode
        self.fd = open(filename, mode)

    def close(self):
        if self.fd:
            self.fd.close()
            self.fd = None

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

class FileRead(File):
    def __init__(self, filename=None):
        super().__init__(filename, 'rb')
        self.mm = None
        self.size = 0
        self.pos = 0
        self.data = b''
        self.data_pos = 0
