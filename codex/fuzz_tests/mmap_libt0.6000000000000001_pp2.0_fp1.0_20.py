import mmap
import os
import re
import sys

from . import util

class ReadLine(object):
    def __init__(self, f, buf_size=16384, limit=None):
        self.f = f
        self.buf_size = buf_size
        self.limit = limit
        self.buf = ""
        self.pos = 0
        self.eof = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.eof:
            raise StopIteration

        if self.limit is not None and self.pos >= self.limit:
            self.eof = True
            raise StopIteration

        if '\n' in self.buf:
            line, self.buf = self.buf.split('\n', 1)
            self.pos += len(line + '\n')
            return line + '\n'

        while True:
            data = self.f.read(self.buf_size)
            self.buf += data
            if len(data) < self.buf_size
