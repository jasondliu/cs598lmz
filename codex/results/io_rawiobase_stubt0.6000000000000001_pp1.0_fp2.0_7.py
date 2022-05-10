import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
        self.f = builtins.open(name, mode)
        self.mode = mode

    def close(self):
        self.f.close()

    def read(self, len):
        return self.f.read(len)

    def write(self, b):
        return self.f.write(b)

    def seek(self, pos, whence):
        return self.f.seek(pos, whence)

    def tell(self):
        return self.f.tell()

    def flush(self):
        return self.f.flush()

    def isatty(self):
        return self.f.isatty()

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return 'r' in self.mode

def open(name, mode='r', **kwargs):
    return File(name, mode)

builtins.open = open

import sys

